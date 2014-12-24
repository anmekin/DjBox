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
//        var parent = $(this).siblings('.comments');
        $.ajax({
            url: '/userfiles_ajax/',
            type: 'get', //this is the default though, you don't actually need to always mention it
            success: function (data) {
                $('#list-files').html(data)
//                parent.html(data)
//                $(this).html(data);
                //alert(data);
            },
            failure: function () {
                alert('Got an error dude');
            }
        })
    },
    function(){
        $('#list-files').empty()
    });

    $('#list-files p').click(
        function() {
            alert("You did it!")
        }
    );
};

$(document).ready(main);

