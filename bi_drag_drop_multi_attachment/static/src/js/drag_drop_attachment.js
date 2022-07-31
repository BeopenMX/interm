odoo.define('bi_drag_drop_multi_attachment.drag_drop_attachment', function(require) {
    "use strict";

    var FormView = require('web.FormView');

    FormView.include({
        init: function (viewInfo, params) {
            var self = this;
            this._super.apply(this, arguments);
            if(self.arch['tag'] == 'form')  {

                console.log(self ,'=============================================$form')

                var isAdvancedUpload = function() {
                    var div = document.createElement('div');
                    return (('draggable' in div) || ('ondragstart' in div && 'ondrop' in div)) && 'FormData' in window && 'FileReader' in window;
                }();
                if (isAdvancedUpload) {
                    var str = '<div class="box" align="center" id="box" >'+
                              '<div class="box-input" id="box-input">'+
                                  '<i class="fa fa-clipboard fa-4x" aria-hidden="true"></i>'+
                                  '<h3><span class="box-dragndrop" id="box-dragndrop">Drag it here</span>.</h4>'+
                              '</div>'+
                              '<div class="box-uploading" id="box-uploading">Uploading</div>'+
                              '<div class="box-success" id="box-success">Done! Upload more</div>'+
                              '<div class="box-error">Error! <span></span>. </div>'+
                              '</div>';

                    if(!$.isEmptyObject(self.mailFields)){
                        $(".o_action_manager").prepend(str);
                        var $form = $('.o_action_manager').find(".box"),
                            $errorMsg = $form.find( '.box-error span' ),
                            $restart = $form.find( '.box-restart' );

                        console.log($form ,'=============================================$form')

                        $form.on('drag dragstart dragend dragover dragenter dragleave drop', function(e) {
                            e.preventDefault();
                            e.stopPropagation();
                        })
                        .on('dragover dragenter', function() {
                            $.FileDialog({multiple: true}).on('files.bs.filedialog', function(ev) {
                                var files = ev.files;
                                var text = "";
                                self
                                files.forEach(function(f) {
                                    var url = self.getUrlVars()

                                    console.log(url,'===================url')

                                    var fd = new FormData();
                                    fd.append("model", url.model);
                                    fd.append("id", url.id);
                                    fd.append("attachment", f);
                                    $.blockUI();
                                    $.ajax({
                                        url: "/drop_attachment",
                                        type: "POST",
                                        data: fd,
                                        dataType: 'json',
                                        cache: false,
                                        contentType: false,
                                        processData: false,
                                        complete: function(data) {
                                            $form.removeClass('is-uploading');
                                            $form.addClass(data.success == true ? 'is-success' : 'is-error');
                                            if (data.success == false) {
                                                $errorMsg.text(data.error_msg);
                                            }
                                        },
                                        success: function(data) {
                                            $.unblockUI();
                                            location.reload();
                                            $form.removeClass('drop-multi-attachment');
                                        },
                                        error: function() {
                                            $.unblockUI();
                                            alert("Error while uploading attachment.");
                                            $form.removeClass('drop-multi-attachment');
                                        }
                                    });
                                    text += f.name + "<br/>";
                                });
                                $("#output").html(text);
                            }).on('cancel.bs.filedialog', function(ev) {
                                $("#output").html("Cancelled!");
                            });
                        })
                    }
                }
            }
        },

        getUrlVars: function()
        {
            var vars = [], hash, hash_1, hash_j;
            var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
            
            console.log(hashes,'=========================hashes')

            for(var i = 0; i < hashes.length; i++)
            {
                if (hashes[i].indexOf('#') >= 0) {
                    hash = hashes[i].split('#')
                    for(var j=0;j<hash.length;j++)
                    {   
                        hash_j = hash[j].split('=');
                        vars.push(hash_j[0]);
                        vars[hash_j[0]] = hash_j[1];
                    }
                }
                else{
                    hash = hashes[i].split('=');
                    vars.push(hash[0]);
                    vars[hash[0]] = hash[1];
                }
            }
            return vars;
        }
    });



});
