$(function () {
            var kanbanCol = $('.panel-body');
            kanbanCol.css('max-height', (window.innerHeight - 150) + 'px');

            var kanbanColCount = parseInt(kanbanCol.length);
            $('.container-fluid').css('min-width', (kanbanColCount * 350) + 'px');

            draggableInit();

           
        });

        function draggableInit() {
            var sourceId;

            $('[draggable=true]').bind('dragstart', function (event) {
                sourceId = $(this).parent().attr('id');
                console.log("sourceId:= "+sourceId);
                event.originalEvent.dataTransfer.setData("text/plain", event.target.getAttribute('id'));
            });

            $('.panel-body').bind('dragover', function (event) {
                event.preventDefault();
            });

            $('.panel-body').bind('drop', function (event) {
                var children = $(this).children();
                var targetId = children.attr('id');
                console.log("targetId:= "+targetId)

                if (sourceId != targetId) {
                    var elementId = event.originalEvent.dataTransfer.getData("text/plain");
                    console.log("elementId "+elementId)
                    change_task(elementId,targetId)
                    $('#processing-modal').modal('toggle'); //before post
                    // Post data 
                    setTimeout(function () {
                        var element = document.getElementById(elementId);
                        children.prepend(element);
                        $('#processing-modal').modal('toggle'); // after post
                    }, 1000);

                }

                event.preventDefault();
            });
        }


        function change_task(elementId,targetId){

            console.log("Inside change_task")
            // console.log(url)
            $.ajax({
            type: "GET",
            url: "/projects/task/status/change/",
            data:{'task_id':elementId,'status':targetId},
            success: function (data){
            },
            error: function(data) {
                alert(data);
            }
        });


        }

        
