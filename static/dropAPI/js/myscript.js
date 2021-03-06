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
    $('#show_files_button').oldtoggle(function() {
        $.ajax({
            url: '/userfiles_ajax/',
            type: 'get',
            success: function (data) {
                $('#list-files').html(data).show('slow');
            },
            failure: function () {
                alert('Got an error dude');
            }
        })
    },
    function(){
        $('#list-files').slideUp('slow',function(){
            $(this).empty();
        });
    });

    $('#list-files').on('click', '.get-link', function() {
        var link = $(this);
        $.ajax({
            url: '/show_file_ajax/',
            type: 'get',
            data: {'name': $(this).siblings('.filename').text()},
            success: function (data) {
                link.html('<a href=' + data + '>Link for share</a>').removeClass('.get-link');
            },
            failure: function () {
                alert('Got an error dude');
            }
        });
    });

    $('#list-files').on('click', '.delete-file', function() {
        var link = $(this);
        $.ajax({
            url: '/delete_file_ajax/',
            type: 'get',
            data: {'name': $(this).siblings('.filename').text()},
            success: function (data) {
                link.parent().remove()
            },
            failure: function () {
                alert('Got an error dude');
            }
        });
    });
};

$(document).ready(main);