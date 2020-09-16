var alUserService = new AlUserService();

function AlUserService() {
  var _this = this;
   _this.MCK_USER_DETAIL_MAP = [];
   _this.MCK_BLOCKED_TO_MAP = [];
  var MCK_GROUP_MEMBER_SEARCH_ARRAY = new Array();
  var USER_BLOCK_URL = "/rest/ws/user/block";
  var USER_DETAIL_URL = "/rest/ws/user/v2/detail";
  var USER_STATUS_URL = "/rest/ws/user/chat/status";

  _this.updateUserStatus = function(params, callback) {
    if (typeof alUserService.MCK_USER_DETAIL_MAP[params.userId] === 'object') {
      var userDetail = alUserService.MCK_USER_DETAIL_MAP[params.userId];
      if (params.status === 0) {
        userDetail.connected = false;
        userDetail.lastSeenAtTime = params.lastSeenAtTime;
      } else if (params.status === 1) {
        userDetail.connected = true;
      }
    } else {
      var userIdArray = new Array();
      userIdArray.push(params.userId);
      if (typeof callback === "function") {
        callback(userIdArray);
      }
    }
  };
  _this.getUserDetail = function(userId) {
    if (typeof alUserService.MCK_USER_DETAIL_MAP[userId] === 'object') {
      return alUserService.MCK_USER_DETAIL_MAP[userId];
    } else {
      return;
    }
  };
  _this.loadUserProfile = function(userId) {
    if (typeof userId !== "undefined") {
      typeof userId !== "string" && (userId = String(userId));
      var userIdArray = [];
      var memberId = '' + userId.split(",")[0];
      userIdArray.push(memberId);
      _this.loadUserProfiles(userIdArray);
    }
  };
  _this.loadUserProfiles = function(userIds, callback) {
    var userIdArray = [];
    if (typeof callback === "function") {
      callback(userIds, userIdArray);
    }
  };
  _this.getUserStatus = function(params, callback) {
    var response = new Object();
    window.Applozic.ALApiService.getUserStatus({
      success: function(data) {
        if (data.users.length > 0) {
          MCK_GROUP_MEMBER_SEARCH_ARRAY = [];
          if (typeof callback === "function") {
            callback(data);
          }
        }
        response.status = "success";
        response.data = data;
        if (params.callback) {
          params.callback(response);
        }
        return;
      },
      error: function() {
        response.status = "error";
        if (params.callback) {
          params.callback(response);
        }
      }
    });
  };
  _this.blockUser = function(userId, isBlock, callback) {
    if (!userId || typeof isBlock === 'undefined') {
      return;
    }
    var data = "userId=" + userId + "&block=" + isBlock;
    mckUtils.ajax({
      url: MCK_BASE_URL + USER_BLOCK_URL,
      type: 'get',
      data: data,
      encryptionKey: window.Applozic.ALApiService.getEncryptionKey(),
      success: function(data) {
        if (typeof data === 'object') {
          if (data.status === 'success') {
            alUserService.MCK_BLOCKED_TO_MAP[userId] = isBlock;
            if (typeof callback === "function") {
              callback(userId);
            }
          }
        }
      },
      error: function() {}
    });
  };
}
