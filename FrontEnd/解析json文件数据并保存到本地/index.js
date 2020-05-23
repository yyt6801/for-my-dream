$(function () {

    var final_json = [];
    var json_buff = {};
    var jsonStr = "";
    //遍历整个json数据，当key == "name" 时，取出对应的数据
    function getAllJson(jsons) {
        for (key in jsons) {
            if (!(jsons[key] instanceof Object)) {
                if (key == "name" && jsons["url"] != undefined) {
                    json_buff.name = jsons[key];
                    json_buff.url = jsons["url"];
                    final_json.push(JSON.parse(JSON.stringify(json_buff)));
                    // final_json.push(json_buff);
                }
            } else {
                getAllJson(jsons[key]); //如果是Object则递归
            }
        }
        jsonStr = JSON.stringify(final_json);
        console.log(jsonStr)
    };
    $("#btn").click(function () {
        alert("test")
        $.getJSON("Bookmarks.json", function (jsons) {
            //调用
            getAllJson(jsons);

            //把jsonStr字符串保存到本地jsonStr.js
            exportRaw('jsonStr.js', jsonStr)

            function fakeClick(obj) {
                var ev = document.createEvent("MouseEvents");
                ev.initMouseEvent("click", true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                obj.dispatchEvent(ev);
            }

            function exportRaw(name, data) {
                var urlObject = window.URL || window.webkitURL || window;
                var export_blob = new Blob([data]);
                var save_link = document.createElementNS("http://www.w3.org/1999/xhtml", "a")
                save_link.href = urlObject.createObjectURL(export_blob);
                save_link.download = name;
                fakeClick(save_link);
            }

        })
    })

})