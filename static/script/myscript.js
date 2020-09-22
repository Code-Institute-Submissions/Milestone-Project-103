$(document).ready(function(){


    /* Ingredients fields on addrecipe */
    $( "#form" ).keypress(function(e) {
        if ( e.which == 13 ) {
            e.preventDefault();
        }
    });

    var next = 1;
    $(".add-more").click(function(e){
        e.preventDefault();
        var addto = "#ingredients" + next;
        var addRemove = "#ingredients" + (next);
        next = next + 1;
        var newIn = '<input autocomplete="off" class="input form-control2" id="ingredients' + next + '" name="ingredients[]" type="text" placeholder="Add ingredient">';
        var newInput = $(newIn);
        var removeBtn = '<button id="remove' + (next - 1) + '" class="btn btn-danger remove-me" >-</button>';
        var removeButton = $(removeBtn);
        $(addto).after(newInput);
        $(addRemove).after(removeButton);
        $("#ingredients" + next).attr('data-source',$(addto).attr('data-source'));
        $("#count").val(next);  
    
        $('.remove-me').click(function(e){
            e.preventDefault();
            var fieldNum = this.id.substr(this.id.lastIndexOf("e")+1);
            var fieldID = "#ingredients" + fieldNum;
            $(this).remove();
            $(fieldID).remove();
        });
    });


    /* Add/remove additional ingredients fields on edit recipe page */ 
    $( "#form" ).keypress(function(e) {
        if ( e.which == 13 ) {
            e.preventDefault();
        }
    });

    var nextadd = 1;
    $(".add-moreadd").click(function(e){
        e.preventDefault();
        var addtoadd = "#ingredientsadd" + nextadd;
        var addRemoveadd = "#ingredientsadd" + (nextadd);
        nextadd = nextadd + 1;
        var newInadd = '<input autocomplete="off" class="input form-control2" id="ingredientsadd' + nextadd + '" name="ingredients[]" type="text" placeholder="Add ingredient">';
        var newInputadd = $(newInadd);
        var removeBtnadd = '<button id="removeadd' + (nextadd - 1) + '" class="btn btn-danger remove-meadd" >-</button>';
        var removeButtonadd = $(removeBtnadd);
        $(addtoadd).after(newInputadd);
        $(addRemoveadd).after(removeButtonadd);
        $("#ingredientsadd" + nextadd).attr('data-source',$(addtoadd).attr('data-source'));
        $("#count").val(nextadd); 

        $('.remove-meadd').click(function(e){
            e.preventDefault();
            var fieldNum = this.id.substr(this.id.lastIndexOf("d")+1);
            var fieldID = "#ingredientsadd" + fieldNum;
            $(this).remove();
            $(fieldID).remove();
        });
    });


    /* Remove ingredients fields already presented on editrecipe page */
    $('.remove-meedit').click(function(e){
        e.preventDefault();
        var fieldNum = this.id.substr(this.id.lastIndexOf("t")+1);
        var fieldID = "#ingredientsedit" + fieldNum;
        $(this).remove();
        $(fieldID).remove();
    });


    /* Method fields on addrecipe */
    $( "#form" ).keypress(function(e) {
        if ( e.which == 13 ) {
            e.preventDefault();
        }
    });

    var nextmethod = 1;
    $(".add-moremethod").click(function(e){
        e.preventDefault();
        var addtomethod = "#method" + nextmethod;
        var addRemovemethod = "#method" + (nextmethod);
        nextmethod = nextmethod + 1;
        var newInmethod = '<input autocomplete="off" class="input form-control2" id="method' + nextmethod + '" name="methods[]" type="text" placeholder="Add method">';
        var newInputmethod = $(newInmethod);
        var removeBtnmethod = '<button id="mremove' + (nextmethod - 1) + '" class="btn btn-danger remove-memethod" >-</button>';
        var removeButtonmethod = $(removeBtnmethod);
        $(addtomethod).after(newInputmethod);
        $(addRemovemethod).after(removeButtonmethod);
        $("#method" + nextmethod).attr('data-source',$(addtomethod).attr('data-source'));
        $("#countmethod").val(nextmethod);  
    
        $('.remove-memethod').click(function(e){
            e.preventDefault();
            var fieldNummethod = this.id.substr(this.id.lastIndexOf("e")+1);
            var fieldIDmethod = "#method" + fieldNummethod;
            $(this).remove();
            $(fieldIDmethod).remove();
        });
    });


    /* Add/remove additional method fields on edit recipe page  */
    $( "#form" ).keypress(function(e) {
        if ( e.which == 13 ) {
            e.preventDefault();
        }
    });

    var nextmethodadd = 1;
    $(".add-moreaddmethod").click(function(e){
        e.preventDefault();
        var addtoaddmethod = "#methodsadd" + nextmethodadd;
        var addRemoveaddmethod = "#methodsadd" + (nextmethodadd);
        nextmethodadd = nextmethodadd + 1;
        var newInaddmethod = '<input autocomplete="off" class="input form-control2" id="methodsadd' + nextmethodadd + '" name="methods[]" type="text" placeholder="Add method">';
        var newInputaddmethod = $(newInaddmethod);
        var removeBtnaddmethod = '<button id="removeaddmethod' + (nextmethodadd - 1) + '" class="btn btn-danger remove-meaddmethod" >-</button>';
        var removeButtonaddmethod = $(removeBtnaddmethod);
        $(addtoaddmethod).after(newInputaddmethod);
        $(addRemoveaddmethod).after(removeButtonaddmethod);
        $("#methodsadd" + nextmethodadd).attr('data-source',$(addtoaddmethod).attr('data-source'));
        $("#countmethod").val(nextmethodadd); 

        $('.remove-meaddmethod').click(function(e){
            e.preventDefault();
            var fieldNum = this.id.substr(this.id.lastIndexOf("d")+1);
            var fieldID = "#methodsadd" + fieldNum;
            $(this).remove();
            $(fieldID).remove();
        });
    });


    /* Remove method fields already presented on editrecipe page */
    $('.remove-meeditmethods').click(function(e){
        e.preventDefault();
        var fieldNum = this.id.substr(this.id.lastIndexOf("d")+1);
        var fieldID = "#methodsedit" + fieldNum;
        $(this).remove();
        $(fieldID).remove();
    });

});