const fs = require('fs');
const path = require('path');
const conf = require('config');
const baseUrl = conf.get('baseUrl');
const applozicMinifiedFileUrl = conf.get('applozicMinifiedFileUrl');
const minify = require('@node-minify/core');
const terser = require('@node-minify/terser');
const noCompress = require('@node-minify/no-compress');
console.log(baseUrl);
const generateBuildFiles = () => {
    minify({
        compressor: terser,
        // To not compress and only concat replace terser -> noCompress
        input: [
            './public/plugin/js/stomp.2.3.3.min.js',
            './public/plugin/js/crypto-js.4.0.min.js',
            './public/plugin/js/app/applozic.common.js',
            './public/plugin/js/app/modules/applozic.chat.js',
            './public/plugin/js/app/modules/storage/applozic.storage.js',
            './public/plugin/js/app/modules/api/applozic.api.js',
            './public/plugin/js/app/modules/socket/applozic.socket.js',
            './public/plugin/js/app/modules/notification/applozic.notification.js',
            './public/plugin/js/app/modules/group/applozic.group.js',
            './public/plugin/js/app/modules/user/applozic.user.js',
            './public/plugin/js/app/modules/file/applozic.file.js',
            './public/plugin/js/app/modules/customFunctions/applozic.custom.js',
            './public/plugin/js/app/modules/label/applozic.label.js', './public/plugin/js/app/modules/message/applozic.message.js'
        ],
        output: './public/applozic.chat.min.js',
        callback: function (err, min) {
            if (err) return console.log(err);
            console.log("applozic.chat.min.js combined successfully");
        }
    });
}

const updateDataAsPerEnv = () => {
    fs.readFile(path.join(__dirname, "/plugin/sample/temp/sideboxtest.html"), 'utf8', function (err, data) {
        if (err) {
            return console.log(err);
        }
        var result = data.replace(":getBaseurl", baseUrl);
        var result = result.replace(":applozicMinifiedFileUrl", applozicMinifiedFileUrl);

        fs.writeFile("./public/plugin/sample/sidebox.html", result, 'utf8', function (err) {
            if (err) return console.log(err);
        });
    });
    fs.readFile(path.join(__dirname, "/plugin/sample/temp/fullviewtest.html"), 'utf8', function (err, data) {
        if (err) {
            return console.log(err);
        }
        var result = data.replace(":getBaseurl", baseUrl);
        var result = result.replace(":applozicMinifiedFileUrl", applozicMinifiedFileUrl);

        fs.writeFile("./public/plugin/sample/fullview.html", result, 'utf8', function (err) {
            if (err) return console.log(err);
        });
    });
    fs.readFile(path.join(__dirname, "/plugin/sample/temp/coretest.html"), 'utf8', function (err, data) {
        if (err) {
            return console.log(err);
        }
        var result = data.replace(":getBaseurl", baseUrl);
        var result = result.replace(":applozicMinifiedFileUrl", applozicMinifiedFileUrl);

        fs.writeFile("./public/plugin/sample/core.html", result, 'utf8', function (err) {
            if (err) return console.log(err);
        });
    });

    fs.readFile(path.join(__dirname, "/demo/root/temp/indextest.js"), 'utf8', function (err, data) {
        if (err) {
            return console.log(err);
        }
        var result = data.replace(":getBaseurl", baseUrl);

        fs.writeFile("./public/demo/index.js", result, 'utf8', function (err) {
            if (err) return console.log(err);
        });
    });
}
module.exports = {
    generateBuildFiles,
    updateDataAsPerEnv
};