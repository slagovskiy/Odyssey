// TAG
//url_tag_get_all = '{% url 'admin_tag_get' 0 %}';
//url_tag_get = '{% url 'admin_tag' %}';
//url_tag_save = '{% url 'admin_tag_save' %}';

function loadTagData()
{
    $('#dataContainer').html('<div class="loader"></div>');
    $.ajax({
        url : url_tag_get_all,
        cashe: false
    }).done(function(data){
        var jdata = jQuery.parseJSON(data);
        var template = $.templates('#dataTagTemplate');
        $('#dataTagContainer').html(template.render(jdata));
    });
}

function editTagData(key)
{
    $.ajax({
        url :url_tag_get + key + '/',
        cashe: false
    }).done(function(data){
        var jdata = jQuery.parseJSON(data);
        var template = $.templates('#dataTagEdit');
        $('#dataTagForm').html(template.render(jdata));
    });

    $('.open-data-form').fancybox({
        padding: 0,
        type: 'inline',
        title: '',
        modal: false,
        autoSize: true
    });
}

function deleteTagItem() {
    $("#dataTagForm form #deleted").val('true');
    saveTagData();
}

function restoreTagItem() {
    $("#dataTagForm form #deleted").val('false');
    saveTagData();
}

function saveTagData() {
    $.ajax({
            type: 'POST',
            url: url_tag_save,
            data: $("#dataTagForm form").serialize()
        })
        .done(function(data){
            if(data=='ok') {
                notice('green', 'saved');
                $.fancybox.close();
                loadTagData();
            }
            else {
                notice('red', data);
            }
        })
        .fail(function(){
            notice('red', 'data transfer error');
        });
    $("#dataTagForm form").submit(function(){
        return false;
    });
}

//CATEGORY
//url_category_get_all = '{% url 'admin_category_get' 0 %}';
//url_category_get = '{% url 'admin_category' %}';
//url_category_save = '{% url 'admin_category_save' %}';


function loadCategoryData()
{
    $('#dataCategoryContainer').html('<div class="loader"></div>');
    $.ajax({
        url : url_category_get_all,
        cashe: false
    }).done(function(data){
        var jdata = jQuery.parseJSON(data);
        var template = $.templates('#dataCategoryTemplate');
        $('#dataCategoryContainer').html(template.render(jdata));
    });

}

function editCategoryData(key)
{
    $.ajax({
        url : url_category_get + key + '/',
        cashe: false
    }).done(function(data){
        var jdata = jQuery.parseJSON(data);
        var template = $.templates('#dataCategoryEdit');
        $('#dataCategoryForm').html(template.render(jdata));
    });

    $('.open-data-form').fancybox({
        padding: 0,
        type: 'inline',
        title: '',
        modal: false,
        autoSize: true
    });
}

function deleteCategoryItem() {
    $("#dataCategoryForm form #deleted").val('true');
    saveCategoryData();
}

function restoreCategoryItem() {
    $("#dataCategoryForm form #deleted").val('false');
    saveCategoryData();
}

function saveCategoryData() {
    $.ajax({
                type: 'POST',
                url:  url_category_save,
                data: $("#dataCategoryForm form").serialize()
            })
            .done(function(data){
                if(data=='ok') {
                    notice('green', 'saved');
                    $.fancybox.close();
                    loadCategoryData();
                }
                else {
                    notice('red', data);
                }
            })
            .fail(function(){
                notice('red', 'data transfer error');
            });
    $("#dataCategoryForm form").submit(function(){
        return false;
    });
}

//MYLINK
//url_mylink_get_all = '{% url 'admin_mylink_get' 0 %}';
//url_mylink_get = '{% url 'admin_mylink' %}';
//url_mylink_save = '{% url 'admin_mylink_save' %}';


function loadLinkData()
{
    $('#dataContainer').html('<div class="loader"></div>');
    $.ajax({
        url : url_mylink_get_all,
        cashe: false
    }).done(function(data){
        var jdata = jQuery.parseJSON(data);
        var template = $.templates('#dataLinkTemplate');
        $('#dataLinkContainer').html(template.render(jdata));
    });
}

function editLinkData(key)
{
    $.ajax({
        url : url_mylink_get + key + '/',
        cashe: false
    }).done(function(data){
        var jdata = jQuery.parseJSON(data);
        var template = $.templates('#dataLinkEdit');
        $('#dataLinkForm').html(template.render(jdata));
    });

    $('.open-data-form').fancybox({
        padding: 0,
        type: 'inline',
        title: '',
        modal: false,
        autoSize: true
    });
}

function deleteLinkItem() {
    $("#dataLinkForm form #deleted").val('true');
    saveLinkData();
}

function restoreLinkItem() {
    $("#dataLinkForm form #deleted").val('false');
    saveLinkData();
}

function saveLinkData() {
    $.ajax({
        type: 'POST',
        url: url_mylink_save,
        data: $("#dataLinkForm form").serialize()
        })
        .done(function(data){
            if(data=='ok') {
                notice('green', 'saved');
                $.fancybox.close();
                loadLinkData();
            }
            else {
                notice('red', data);
            }
        })
        .fail(function(){
            notice('red', 'data transfer error');
        });
$("#dataLinkForm form").submit(function(){
        return false;
    });
}

//FOLDER
//url_folder_get_all = '{% url 'admin_folder_get' 0 %}';
//url_folder_get = '{% url 'admin_folder' %}';
//url_files_get = '{% url 'admin_files' %}';
//url_file_get = '{% url 'admin_file' %}';
//url_folder_save = '{% url 'admin_folder_save' %}';

function loadFolderData()
{
    $('#dataFolderContainer').html('<div class="loader"></div>');
    $('#dataFolderContainerImages').html('');
    $.ajax({
        url : url_folder_get_all,
        cashe: false
    }).done(function(data){
        var jdata = jQuery.parseJSON(data);
        var template = $.templates('#dataFolderTemplate');
        $('#dataFolderContainer').html(template.render(jdata));
    });
}

function editFolderData(key)
{
    $.ajax({
        url : url_folder_get + key + '/',
        cashe: false
    }).done(function(data){
        var jdata = jQuery.parseJSON(data);
        var template = $.templates('#dataFolderEdit');
        $('#dataFolderForm').html(template.render(jdata));
    });

    $('.open-data-form').fancybox({
        padding: 0,
        type: 'inline',
        title: '',
        modal: false,
        autoSize: true
    });
}

function deleteFolderItem() {
    $("#dataFolderForm form #deleted").val('true');
    saveFolderData();
}

function restoreFolderItem() {
    $("#dataFolderForm form #deleted").val('false');
    saveFolderData();
}

function saveFolderData() {
    $.ajax({
        type: 'POST',
        url: url_folder_save,
        data: $("#dataFolderForm form").serialize()
        })
        .done(function(data){
            if(data=='ok') {
                notice('green', 'saved');
                $.fancybox.close();
                loadFolderData();
            }
            else {
                notice('red', data);
            }
        })
        .fail(function(){
            notice('red', 'data transfer error');
        });
$("#dataFolderForm form").submit(function(){
        return false;
    });
}


function loadFolderImagesData(key)
{
    $('#dataFolderContainer').html('<div class="loader"></div>');
    $.ajax({
        url : url_folder_get + key + '/',
        cashe: false
    }).done(function(data){
        var jdata = jQuery.parseJSON(data);
        var template = $.templates('#dataFolderUpload');
        $('#dataFolderContainer').html(template.render(jdata));
        initUpload();
        loadFolderImages(key);
    });
}

function loadFolderImages(key)
{
    $('#dataContainerImages').html('<div class="loader"></div>');
    $.ajax({
        url : url_files_get + key + '/',
        cashe: false
    }).done(function(data){
        var jdata = jQuery.parseJSON(data);
        var template = $.templates('#dataFolderImages');
        $('#dataFolderContainerImages').html(template.render(jdata));
    });
}

function deleteFolderImage(key)
{
    $.ajax({
        url : url_file_get + key + '/?action=delete',
        cashe: false
    }).done(function(data){
        if (data=='ok')
        {
            $('#imageItem' + key).hide();
            notice('green', 'file deleted');
        }
    });
}



$(document).ready(function() {
    $('.dateMask').mask('0000/00/00');
    $('.datetimeMask').mask('0000/00/00 00:00:00');

    $.views.converters({
        datetime: function(value) {
            if ((value == '') || (value == null))
                return value;
            else {
                var date = '/';
                var time = ':';
                if (this.tagCtx.props.date)
                    date = this.tagCtx.props.date;
                if (this.tagCtx.props.time)
                    time = this.tagCtx.props.time;
                var dt = value.split('T');
                var d = dt[0].split('-');
                var t = dt[1].replace('T', '').replace('Z', '').split(':');
                return d[0] + date + d[1] + date + d[2] + ' ' + t[0] + time + t[1] + time + t[2].split('.')[0];
            }
        }
    });

    $.views.tags({
        cutstr: function () {
            var ln = 20;
            var str = this.tagCtx.render();
            if (this.tagCtx.props.max)
                ln = this.tagCtx.props.max;
            if (str.length > ln)
                return  str.substr(0, ln - 1) + "...";
            else
                return str;
        }
    });

});
