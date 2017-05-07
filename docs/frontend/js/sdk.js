var Pic2Emoji = function(api_url){
    // Set API location
    this.api_url = api_url;
    this.username = null;
    this.autoSendMessage = function(text){
        var self = this;
        var text = text;
        $.ajax({
            type: "HEAD",
            url : text,
            success: function(message,rsp_text,response){
                if(response.getResponseHeader('Content-Type').indexOf("image")!=-1){
                    // POST image to server
                    self.sendMessage(text, "photo");
                }
            },
            error: function(){
                // POST text to server
                self.sendMessage(text, "text");
            }
        });
    }

    this.sendMessage = function(text, type){
        $("#send-button").attr("disabled", true);
        $("#upload-image-button").attr("disabled", true);
        $("#send-button").html("<i class='fa fa-spinner fa-spin'></i> 正在发送");
        var d = new Date();
        var data = {
            date: d.toJSON(),
            username: this.username
        }
        if(type == "text"){
            data.type = "text";
            data.text = text;
        } else if(type == "photo"){
            data.type = "photo";
            data.photo = text;
        } else {
            throw new Error("invalid message type");
        }
        $.ajax({
            type: "POST",
            url: this.api_url + "/chat/message",
            data: JSON.stringify(data),
            dataType:"json",
            contentType:"application/json",
            success: function(){
                // Message sent
                $("#upload-image-button").attr("disabled", false);
                $("#send-button").attr("disabled", false);
                $("#send-button").html("<i class='fa fa-paper-plane'></i> 发送");
            },
            error: function(){
                // Failed to send image
                alert("failed to send message");
                $("#send-button").attr("disabled", false);
                $("#send-button").attr("disabled", false);
                $("#send-button").html("<i class='fa fa-paper-plane'></i> 发送");
            }
        });
    }

    this.getMessages = function(since, callback){
        var callback = callback;
        if(this.get_request != null){
            this.get_request.abort();
        }
        this.get_request = $.ajax({
            type:"GET",
            url: this.api_url + "/chat/message?since=" + since,
            dataType:"json",
            success: function(data){
                // Process data here
                callback(data);
            },
            error: function(){
                // this should not happen....
            }
        })
    }

    this.setCookie = function(cname, cvalue, exdays){
        var d = new Date();
        d.setTime(d.getTime() + (exdays*24*60*60*1000));
        var expires = "expires="+ d.toUTCString();
        document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    }

    this.getCookie = function(cname){
        var name = cname + "=";
        var decodedCookie = decodeURIComponent(document.cookie);
        var ca = decodedCookie.split(';');
        for(var i = 0; i <ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return null;
    }

    this.checkUsername = function(username){
        if(username == null || username.length > 10 || username.length <= 0){
            return false;
        }
        return true;
    }

    this.getUsername = function(){
        this.username = decodeURIComponent(window.location.hash.substr(1));
        //first_load_finished = false;
        if(this.checkUsername(this.username)) reloadMessages(false);
        $("#msg-textbox").attr("placeholder", "输入你的信息 (" + this.username + ")");
    }

    this.setUsername = function(username){
        if(this.checkUsername(username)){
            window.location.hash = username;
            this.getUsername();
            first_load_finished = false;
            reloadMessages(false);
        }
    }


    this.init = function(){
        this.getUsername();
        if(!this.checkUsername(this.username)){
            // Force user to choose an username
            $("#username-modal").modal({
                backdrop:'static'
            });
        }
    }

}