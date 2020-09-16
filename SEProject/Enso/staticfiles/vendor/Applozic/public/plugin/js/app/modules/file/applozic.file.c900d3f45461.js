// File related functions
var alFileService = new AlFileService();

function AlFileService() {
  var _this = this;

  var ONE_KB = 1024;
  var ONE_MB = 1048576;
  var UPLOAD_VIA = ['CREATE', 'UPDATE'];
  var FILE_PREVIEW_URL = "/rest/ws/aws/file/";
  var FILE_UPLOAD_URL = "/rest/ws/aws/file/url";
  var FILE_AWS_UPLOAD_URL = "/rest/ws/upload/file";
  var FILE_DELETE_URL = "/rest/ws/aws/file/delete";
  var CLOUD_HOST_URL = "www.googleapis.com";
  var MCK_STORAGE_URL ;
  var MCK_FILE_URL ;
  var MCK_MAP_STATIC_API_KEY ;
  var MCK_CUSTOM_UPLOAD_SETTINGS ;
  var MCK_APP_ID;
  var AUTH_CODE;
  var USER_DEVICE_KEY;
  var MCK_ACCESS_TOKEN;
  var MCK_APP_MODULE_NAME;
  var MCK_GENERATE_CLOUD_FILE_URL;

  _this.init = function(optns) {
    MCK_FILE_URL = optns.fileBaseUrl;
    AUTH_CODE = btoa(optns.userId + ':' + optns.deviceKey);
    USER_DEVICE_KEY = optns.deviceKey;
  };

  _this.get = function(optns) {
    MCK_APP_ID = optns.appId;
    MCK_STORAGE_URL = optns.customUploadUrl;
    MCK_CUSTOM_UPLOAD_SETTINGS = optns.fileupload;
    MCK_MAP_STATIC_API_KEY = optns.mapStaticAPIkey;
    MCK_ACCESS_TOKEN = optns.accessToken;
    MCK_APP_MODULE_NAME = optns.appModuleName;
    MCK_GENERATE_CLOUD_FILE_URL = optns.genereateCloudFileUrl;
  }

  _this.deleteFileMeta = function(blobKey) {
    window.Applozic.ALApiService.deleteFileMeta({
      data: {
        blobKey: blobKey,
        url: MCK_FILE_URL + FILE_DELETE_URL + '?key=' + blobKey,
      },
      success: function(response) {
        console.log(response);
      },
      error: function() {}
    });
  };

  _this.getFilePreviewPath = function(fileMeta) {
    return (typeof fileMeta === "object") ? '<a href="' + MCK_FILE_URL + FILE_PREVIEW_URL + fileMeta.blobKey + '" target="_blank">' + fileMeta.name + '</a>' : '';
  };

  _this.getFilePreviewSize = function(fileSize) {
    if (fileSize) {
      if (fileSize > ONE_MB) {
        return "(" + parseInt(fileSize / ONE_MB) + " MB)";
      } else if (fileSize > ONE_KB) {
        return "(" + parseInt(fileSize / ONE_KB) + " KB)";
      } else {
        return "(" + parseInt(fileSize) + " B)";
      }
    }
    return '';
  };

  _this.getFileurl = function(msg) {
  if (typeof msg.fileMeta === "object") {
    if ((msg.fileMeta).hasOwnProperty("url")) {
      if (((msg.fileMeta.url).indexOf(CLOUD_HOST_URL) !== -1)) {
        var fileUrl;
        _this.generateCloudUrl(msg.fileMeta.blobKey,function(result){
          fileUrl= result;
        });
        return fileUrl;
      } else {
        return '' + msg.fileMeta.url;
      }
    } else if ((msg.fileMeta.thumbnailUrl === "thumbnail_" + msg.fileMeta.name)) {
      return MCK_STORAGE_URL + "/files/" + msg.fileMeta.name;
    } else {
      return MCK_FILE_URL + FILE_PREVIEW_URL + msg.fileMeta.blobKey;
    }
  }
    return '';
  };

_this.generateCloudUrl = function(key, callback) {
  // Custom function for generating image url for google cloud server
  var url = MCK_GENERATE_CLOUD_FILE_URL.replace("{key}",key);
  var headers = window.Applozic.ALApiService.getAttachmentHeaders();
  mckUtils.ajax({
      type: 'get',
      async: false,
      skipEncryption: true,
      headers: headers,
      url: url,
      success: function(result) {
        if (typeof callback === "function") {
          callback(result);
        }
      },
      error: function(result) {
          console.log("error while getting token" + result);
      }
  });
};

  _this.getFilePath = function(msg) {
    if (msg.contentType === 2) {
      try {
        var geoLoc = JSON.parse(msg.message);
        if (geoLoc.lat && geoLoc.lon) {
          return '<a href="http://maps.google.com/maps?z=17&t=m&q=loc:' + geoLoc.lat + "," + geoLoc.lon + '" target="_blank"><img src="https://maps.googleapis.com/maps/api/staticmap?zoom=17&size=200x150&center=' + geoLoc.lat + "," + geoLoc.lon + '&maptype=roadmap&markers=color:red|' + geoLoc.lat + "," + geoLoc.lon + '&key=' + MCK_MAP_STATIC_API_KEY + '"/></a>';
        }
      } catch (ex) {
        if (msg.message.indexOf(',') !== -1) {
          return '<a href="http://maps.google.com/maps?z=17&t=m&q=loc:' + msg.message + '" target="_blank"><img src="https://maps.googleapis.com/maps/api/staticmap?zoom=17&size=200x150&center=' + msg.message + '&maptype=roadmap&markers=color:red|' + msg.message + '&key=' + MCK_MAP_STATIC_API_KEY + '" /></a>';
        }
      }
    }
    if (typeof msg.fileMeta === "object") {
      if (msg.fileMeta.contentType.indexOf("image") !== -1) {
        if (msg.fileMeta.contentType.indexOf("svg") !== -1) {
          return '<a href="#" role="link" target="_self" class="file-preview-link fancybox-media imageview" data-type="' + msg.fileMeta.contentType + '" data-url="' + _this.getFileurl(msg) + '" data-name="' + msg.fileMeta.name + '"><img src="' + _this.getFileurl(msg) + '" area-hidden="true"></img></a>';
        } else if (msg.contentType === 5) {
          return '<a href="#" role="link" target="_self" class="file-preview-link fancybox-media imageview" data-type="' + msg.fileMeta.contentType + '" data-url="' + msg.fileMeta.blobKey + '" data-name="' + msg.fileMeta.name + '"><img src="' + msg.fileMeta.blobKey + '" area-hidden="true"></img></a>';
        } else {
            if((msg.fileMeta).hasOwnProperty("url")){
              if((msg.fileMeta.url).indexOf(CLOUD_HOST_URL) !== -1){
                // Google Cloud Server
                var thumbnailUrl ;
                _this.generateCloudUrl(msg.fileMeta.thumbnailBlobKey, function(result) {
                  thumbnailUrl= result;
                });
                return '<a href="#" role="link" target="_self" class="file-preview-link fancybox-media imageview" data-type="' + msg.fileMeta.contentType + '" data-url="" data-blobKey="' + msg.fileMeta.blobKey + '" data-name="' + msg.fileMeta.name + '"><img src="' + thumbnailUrl + '" area-hidden="true"></img></a>';
              }
              else {
                return '<a href="#" role="link" target="_self" class="file-preview-link fancybox-media imageview" data-type="' + msg.fileMeta.contentType + '" data-url="' + _this.getFileurl(msg) + '" data-name="' + msg.fileMeta.name + '"><img src="' + msg.fileMeta.thumbnailUrl + '" area-hidden="true"></img></a>';
              }
            }
            else if((msg.fileMeta.thumbnailUrl === "thumbnail_"+msg.fileMeta.name )){
            return '<a href="#" role="link" target="_self" class="file-preview-link fancybox-media imageview" data-type="' + msg.fileMeta.contentType + '" data-url="' + _this.getFileurl(msg) + '" data-name="' + msg.fileMeta.name + '"><img src="' + MCK_STORAGE_URL + "/files/thumbnail_" + msg.fileMeta.name + '" area-hidden="true"></img></a>';
            }
            else {
            return '<a href="#" role="link" target="_self" class="file-preview-link fancybox-media imageview" data-type="' + msg.fileMeta.contentType + '" data-url="' + _this.getFileurl(msg) + '" data-name="' + msg.fileMeta.name + '"><img src="' + msg.fileMeta.thumbnailUrl + '" area-hidden="true"></img></a>';
          }
        }
      } else if (msg.fileMeta.contentType.indexOf("video") !== -1) {
        if(((msg.fileMeta).hasOwnProperty("url")) && ((msg.fileMeta.url).indexOf(CLOUD_HOST_URL) !== -1)){
          // Google Cloud Server
          var getUrl ;
          _this.generateCloudUrl(msg.fileMeta.blobKey, function(result) {
            getUrl= result;
          });
          return '<a href="#" target="_self"><video controls class="mck-video-player" onplay="alFileService.updateAudVidUrl(this);" data-cloud-service="google_cloud" data-blobKey="' + msg.fileMeta.blobKey + '">' + '<source src="' + getUrl + '" type="video/mp4">' + '<source src="' + getUrl + '" type="video/ogg"></video>';
        }
        else{
          return '<a href= "#" target="_self"><video controls class="mck-video-player">' + '<source src="' + _this.getFileurl(msg) + '" type="video/mp4">' + '<source src="' + _this.getFileurl(msg) + '" type="video/ogg"></video></a>';
        }        //    return '<a href="#" role="link" class="file-preview-link fancybox-media fancybox" data-type="' + msg.fileMeta.contentType + '" data-url="' + MCK_FILE_URL + FILE_PREVIEW_URL + msg.fileMeta.blobKey + '" data-name="' + msg.fileMeta.name + '"><div class="mck-video-box n-vis"><video controls preload><source src="' + MCK_FILE_URL + FILE_PREVIEW_URL + msg.fileMeta.blobKey + '" type="' + msg.fileMeta.contentType + '"></video></div><span class="file-detail"><span class="mck-file-name"><span class="mck-icon-attachment"></span>&nbsp;' + msg.fileMeta.name + '</span>&nbsp;<span class="file-size">' + mckFileService.getFilePreviewSize(msg.fileMeta.size) + '</span></span></a>';
      } else if (msg.fileMeta.contentType.indexOf("audio") !== -1) {
        if(((msg.fileMeta).hasOwnProperty("url")) && ((msg.fileMeta.url).indexOf(CLOUD_HOST_URL) !== -1)){
          var getUrl ;
          _this.generateCloudUrl(msg.fileMeta.blobKey, function(result) {
            getUrl= result;
          });
          return '<a href="#" target="_self"><audio controls class="mck-audio-player" onplay="alFileService.updateAudVidUrl(this);" data-cloud-service="google_cloud" data-blobKey="' + msg.fileMeta.blobKey + '">' + '<source src="' + getUrl + '" type="audio/ogg">' + '<source src="' + getUrl + '" type="audio/mpeg"></audio>' + '<p class="mck-file-tag"></p></a>';
        }
        else {
        return '<a href="#" target="_self"><audio controls class="mck-audio-player">' + '<source src="' + _this.getFileurl(msg) + '" type="audio/ogg">' + '<source src="' + _this.getFileurl(msg) + '" type="audio/mpeg"></audio>' + '<p class="mck-file-tag"></p></a>';
      }
      } else {
        return '<a href="#" role="link" class="file-preview-link" target="_self"></a>';
      }
    }
    return '';
  };

  _this.updateAudVidUrl = function (element){
      var keygen = element.dataset.blobkey;
      var time = new Date().getTime();
      var currentSrc= element.currentSrc;
      var expiry= _this.fetchQueryString("Expires", currentSrc);
      if(time >= (expiry*1000)){
        _this.generateCloudUrl(keygen, function(result) {
            getUrl= result;
        });
      element.src=getUrl;
    }
  };

  this.fetchQueryString = function(regKey, href) {
    regKey = regKey.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regexValue = new RegExp("[\\?&]" + regKey + "=([^&#]*)");
    var result = regexValue.exec(href);
    if (result == null) {
      console.log("The parameter is null for the searchedquery");
    }
    return (result[1]);
  };

  _this.getFileAttachment = function (msg) {
      if (typeof msg.fileMeta === 'object') {
          //var srcUrl=msg.fileMeta.hasOwnProperty("url")? msg.fileMeta:MCK_FILE_URL + FILE_PREVIEW_URL + msg.fileMeta.blobKey;
          if (msg.fileMeta.contentType.indexOf("image") !== -1 || (msg.fileMeta.contentType.indexOf("audio") !== -1) || (msg.fileMeta.contentType.indexOf("video") !== -1)) {
              if((msg.fileMeta).hasOwnProperty("url") && ((msg.fileMeta.url).indexOf(CLOUD_HOST_URL) !== -1)){
                return '<a href="javascript:void(0);" role="link" target="_self"  class="file-preview-link" data-blobKey="' + msg.fileMeta.blobKey + '" data-cloud-service="google_cloud"><span class="file-detail mck-image-download"><span class="mck-file-name"><span class="mck-attachement-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20"><g data-name="Group 122"><path fill="none" d="M0 0h24v24H0z" data-name="Rectangle 1"/><path d="M19.00483767 16.29529691l-11.90272845-.0417193a4.358 4.358 0 0 1-4.32607928-4.32607929A4.259 4.259 0 0 1 7.0483691 7.65515915l10.48639356.03394113v.70710678L7.07241074 8.3382243a3.61826547 3.61826547 0 1 0 .00141421 7.2365308l11.89990002.03889087a2.647 2.647 0 0 0 2.68700577-2.68700576 2.688 2.688 0 0 0-2.70680476-2.70680476l-10.15476048-.0615183a1.774 1.774 0 0 0-1.75998878 1.75998879 1.8 1.8 0 0 0 1.76776695 1.76776695l8.82681395.02899138v.70710678l-8.81832866-.02333453a2.491 2.491 0 0 1-2.47840927-2.47840926 2.46 2.46 0 0 1 2.46426713-2.46426714l10.18375186.0311127a3.462 3.462 0 0 1 3.4400745 3.4400745 3.424 3.424 0 0 1-3.4202755 3.3679496z" data-name="Path 1"/></g></svg></span>&nbsp;' + msg.fileMeta.name + '</span>&nbsp;<span class="file-size">' + alFileService.getFilePreviewSize(msg.fileMeta.size) + '</span></span></a>';
              }
            else {
              return '<a href="' + _this.getFileurl(msg) + '" role="link" target="_self"  class="file-preview-link"><span class="file-detail mck-image-download"><span class="mck-file-name"><span class="mck-attachement-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20"><g data-name="Group 122"><path fill="none" d="M0 0h24v24H0z" data-name="Rectangle 1"/><path d="M19.00483767 16.29529691l-11.90272845-.0417193a4.358 4.358 0 0 1-4.32607928-4.32607929A4.259 4.259 0 0 1 7.0483691 7.65515915l10.48639356.03394113v.70710678L7.07241074 8.3382243a3.61826547 3.61826547 0 1 0 .00141421 7.2365308l11.89990002.03889087a2.647 2.647 0 0 0 2.68700577-2.68700576 2.688 2.688 0 0 0-2.70680476-2.70680476l-10.15476048-.0615183a1.774 1.774 0 0 0-1.75998878 1.75998879 1.8 1.8 0 0 0 1.76776695 1.76776695l8.82681395.02899138v.70710678l-8.81832866-.02333453a2.491 2.491 0 0 1-2.47840927-2.47840926 2.46 2.46 0 0 1 2.46426713-2.46426714l10.18375186.0311127a3.462 3.462 0 0 1 3.4400745 3.4400745 3.424 3.424 0 0 1-3.4202755 3.3679496z" data-name="Path 1"/></g></svg></span>&nbsp;' + msg.fileMeta.name + '</span>&nbsp;<span class="file-size">' + alFileService.getFilePreviewSize(msg.fileMeta.size) + '</span></span></a>';
            }
          } else {
              return '<a href="' + _this.getFileurl(msg) + '" role="link" target="_self"  class="file-preview-link"><span class="file-detail mck-image-download"><span class="mck-file-name"><span class="mck-attachement-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20"><g data-name="Group 122"><path fill="none" d="M0 0h24v24H0z" data-name="Rectangle 1"/><path d="M19.00483767 16.29529691l-11.90272845-.0417193a4.358 4.358 0 0 1-4.32607928-4.32607929A4.259 4.259 0 0 1 7.0483691 7.65515915l10.48639356.03394113v.70710678L7.07241074 8.3382243a3.61826547 3.61826547 0 1 0 .00141421 7.2365308l11.89990002.03889087a2.647 2.647 0 0 0 2.68700577-2.68700576 2.688 2.688 0 0 0-2.70680476-2.70680476l-10.15476048-.0615183a1.774 1.774 0 0 0-1.75998878 1.75998879 1.8 1.8 0 0 0 1.76776695 1.76776695l8.82681395.02899138v.70710678l-8.81832866-.02333453a2.491 2.491 0 0 1-2.47840927-2.47840926 2.46 2.46 0 0 1 2.46426713-2.46426714l10.18375186.0311127a3.462 3.462 0 0 1 3.4400745 3.4400745 3.424 3.424 0 0 1-3.4202755 3.3679496z" data-name="Path 1"/></g></svg></span>&nbsp;' + msg.fileMeta.name + '</span>&nbsp;<span class="file-size">' + alFileService.getFilePreviewSize(msg.fileMeta.size) + '</span></span></a>';
          }
          return '';
      }
  };

  _this.getFileIcon = function(msg) {
    if (msg.fileMetaKey && typeof msg.fileMeta === 'object') {
      if (msg.fileMeta.contentType.indexOf('image') !== -1) {
        return '<span class="mck-icon--camera"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3.2" fill="rgba(38,50,56,.52)"/><path d="M9 2L7.17 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2h-3.17L15 2H9zm3 15c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5z" fill="rgba(38,50,56,.52)"/><path d="M0 0h24v24H0z" fill="none"/></svg></span>&nbsp;<span>Image</span>'
      } else if (msg.fileMeta.contentType.indexOf('audio') !== -1) {
        return '<span class="mck-attachement-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20"><g data-name="Group 122"><path fill="none" d="M0 0h24v24H0z" data-name="Rectangle 1"/><path d="M19.00483767 16.29529691l-11.90272845-.0417193a4.358 4.358 0 0 1-4.32607928-4.32607929A4.259 4.259 0 0 1 7.0483691 7.65515915l10.48639356.03394113v.70710678L7.07241074 8.3382243a3.61826547 3.61826547 0 1 0 .00141421 7.2365308l11.89990002.03889087a2.647 2.647 0 0 0 2.68700577-2.68700576 2.688 2.688 0 0 0-2.70680476-2.70680476l-10.15476048-.0615183a1.774 1.774 0 0 0-1.75998878 1.75998879 1.8 1.8 0 0 0 1.76776695 1.76776695l8.82681395.02899138v.70710678l-8.81832866-.02333453a2.491 2.491 0 0 1-2.47840927-2.47840926 2.46 2.46 0 0 1 2.46426713-2.46426714l10.18375186.0311127a3.462 3.462 0 0 1 3.4400745 3.4400745 3.424 3.424 0 0 1-3.4202755 3.3679496z" data-name="Path 1"/></g></svg></span>&nbsp;<span>Audio</span>';
      } else if (msg.fileMeta.contentType.indexOf('video') !== -1) {
        return '<span class="mck-icon--video"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="22" height="22"><path fill="rgba(38,50,56,.52)" d="M17 10.5V7c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1v-3.5l2.29 2.29c.63.63 1.71.18 1.71-.71V8.91c0-.89-1.08-1.34-1.71-.71L17 10.5z"/></svg></span>&nbsp;<span class="mck-icon-video-text">Video</span>';
      } else {
        return '<span class="mck-attachement-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20"><g data-name="Group 122"><path fill="none" d="M0 0h24v24H0z" data-name="Rectangle 1"/><path d="M19.00483767 16.29529691l-11.90272845-.0417193a4.358 4.358 0 0 1-4.32607928-4.32607929A4.259 4.259 0 0 1 7.0483691 7.65515915l10.48639356.03394113v.70710678L7.07241074 8.3382243a3.61826547 3.61826547 0 1 0 .00141421 7.2365308l11.89990002.03889087a2.647 2.647 0 0 0 2.68700577-2.68700576 2.688 2.688 0 0 0-2.70680476-2.70680476l-10.15476048-.0615183a1.774 1.774 0 0 0-1.75998878 1.75998879 1.8 1.8 0 0 0 1.76776695 1.76776695l8.82681395.02899138v.70710678l-8.81832866-.02333453a2.491 2.491 0 0 1-2.47840927-2.47840926 2.46 2.46 0 0 1 2.46426713-2.46426714l10.18375186.0311127a3.462 3.462 0 0 1 3.4400745 3.4400745 3.424 3.424 0 0 1-3.4202755 3.3679496z" data-name="Path 1"/></g></svg></span>&nbsp;<span>File</span>';
      }
    } else {
      return '';
    }
  };

  _this.downloadfile = function() {
    var url = _this.getFileurl(msg);
    var link = document.createElement("a");
    link.download = thefilename;
    link.setAttribute('href', url);
    // Construct the uri
    var uri = 'data:text/csv;charset=utf-8;base64,' + someb64data
    link.href = uri;
    document.body.appendChild(link);
    link.click();
    // Cleanup the DOM
    document.body.removeChild(link);
  };
}
