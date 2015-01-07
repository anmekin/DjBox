/**
 * Created by andrey on 24.12.14.
 */
$.fn.oldtoggle = function () {
    var b = arguments;
    return this.each(function (i, el) {
        a = function () {
            var c = 0;
            return function () {
                b[c++ % b.length].apply(el, arguments)
            }
        }();
        $(el).click(a)
    })
};

var main=function() {
    $('#test-button').click(function () {
        $.ajax({
            url: '/button_test/',
            type: 'get', //this is the default though, you don't actually need to always mention it
            dataType: 'json',
            success: function (data) {
                $('#test-button').html(data['test']);
                alert(data['test']);
            },
            failure: function (data) {
                alert('Got an error dude');
            }
        });
    });


    $('#show_files_button').oldtoggle(function() {
        $.ajax({
            url: '/userfiles_ajax/',
            type: 'get', //this is the default though, you don't actually need to always mention it
            success: function (data) {
                $('#list-files').html(data)
            },
            failure: function () {
                alert('Got an error dude');
            }
        })
    },
    function(){
        $('#list-files').empty()
    });

    $('#list-files').on('click', 'li', function() {
        var li = $(this)
        $.ajax({
            url: '/show_file_ajax/',
            type: 'get', //this is the default though, you don't actually need to always mention it
            data: {'name': li.text()},
            success: function (data) {
//                alert(li.html()+'q');
                li.append('   <a href='+data+">Link for share</a>");
            },
            failure: function () {
                alert('Got an error dude');
            }
        });
        }
    );
};

$(document).ready(main);

// live(),delegate
// RPC