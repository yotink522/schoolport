$(document).ready(function(){
    /* ----------------------------------- Choose Course 처리부 시작 ------------------------------------------------*/
    var course_table = $('#id_dt_choose_course').DataTable( {
        paging: false
    } );
    //Choose a Course단추를 눌렀을때 처리부
    $(document).on("click", "#btn_regstudent_choose_course", function(e){
        var ids = [];
        $('input[name="course_pks"]').each(function(){
            ids.push(this.value);
        });

        var ctrl = $(this);
        e.preventDefault();
        course_table.destroy();

        course_table = $('#id_dt_choose_course').DataTable( {
            ajax: { 
                "url" : ctrl.attr("ajaxurl"),
                "data": {
                },
            },
            'columnDefs': [{
                'targets': 0,
                'searchable': false,
                'orderable': false,
                'className': 'dt-body-center',
                'render': function (data, type, full, meta){
                    return '<input type="checkbox" name="course_id[]" value="' + $('<div/>').text(data).html() + '">';
                }
             }],
             'order': [[1, 'asc']],
            columns: [
                {"data": "id"},
                {"data": "course_name"},
                {"data": "course_type"},
                {"data": "price"}
            ],
            "drawCallback": function(settings){
                course_table.$('input[name="course_id[]"]').each(function(){
                    if (ids.indexOf(this.value) !== -1){
                        $(this).prop("checked", true);
                    }
                });
            }
        });
    });

    $('#th-select-all-courses').on('click', function(){
        // Get all rows with search applied
        var rows = course_table.rows({ 'search': 'applied' }).nodes();
        // Check/uncheck checkboxes for all rows in the table
        $('input[type="checkbox"]', rows).prop('checked', this.checked);
    });

    // Handle click on checkbox to set state of "Select all" control
    $('#id_dt_choose_course tbody').on('change', 'input[type="checkbox"]', function(){
        // If checkbox is not checked
        if(!this.checked){
           var el = $('#th-select-all-courses').get(0);
           // If "Select all" control is checked and has 'indeterminate' property
           if(el && el.checked && ('indeterminate' in el)){
              // Set visual state of "Select all" control
              // as 'indeterminate'
              el.indeterminate = true;
           }
        }
    });

    // 강좌선택모달에서 선택된 강좌들을 메인테이블에 그리기 
    $(document).on('click', '#id-btn-choose-course-select', function(e){
        var course_ids = [];
        e.preventDefault();
        // Iterate over all checkboxes in the table
        //course_table.$('input[type="checkbox"]').each(function(){
        course_table.$('input[name="course_id[]"]').each(function(){
            // If checkbox doesn't exist in DOM
            //if(!$.contains(document, this)){
                // If checkbox is checked
                if(this.checked){
                    //console.log(this.name + ":" + this.value);
                    course_ids.push(this.value);
                    /*
                    // Create a hidden element
                    $(form).append(
                        $('<input>')
                        .attr('type', 'hidden')
                        .attr('name', this.name)
                        .val(this.value)
                    );
                    */
                }
            //}
        });

        $.ajax({
            url: "get_course_list", //선택된 강좌의 primary key값(배렬)들을 가지고 DB에 조회하기
            type: 'post',
            dataType: 'json',
            data : JSON.stringify(course_ids), //자바스크립트 배렬을 JSON형태로 변환하기
            beforeSend: function () {
            },
            success: function (resp) {
                $('#table_purchased_info .tr_courses').remove(); //이미전에 추가된 tr 모두 삭제하기 
                
                json_result = JSON.parse(resp); //결과로 넘어온 json_string 을 javascript json 오브젝트로 변환하기 
                json_result.forEach(function(course){
                    console.log(course.pricing_standards);

                    var innerHtml =  "<tr class='tr_courses'>";
                    innerHtml += '<input type="hidden" name="course_pks" value="' + course.id + '">';
                    innerHtml += '<td>' + course.course_name + '</td>';

                    innerHtml += '<td><select>';
                    pricing_standards = JSON.parse(course.pricing_standards);
                    pricing_standards.forEach(function(std){
                        innerHtml += '<option value='+ std.pk +'>' + std.fields.price + ' ' + std.fields.price_currency + '/' + std.fields.price_unit + '</option>';
                    });
                    innerHtml += '</select></td>';

                    //innerHtml += '<td>' + course.price + ' ' + course.price_currency + '/' + course.price_unit + '</td>';
                    innerHtml += '<td><input type="text" value="' + course.price + '">/' + course.price_unit + '</td>';
                    innerHtml += '<td><input type="text">Months</td>';
                    innerHtml += '<td>0.00 yuan</td>';
                    innerHtml += '<td><input type="text">day</td>';
                    innerHtml += '<td><input type="text"></td>';
                    innerHtml += '</tr>';
                    $('#table_purchased_info > tbody:last').append(innerHtml);

                });
            }
        });
    });
    /* ----------------------------------- Choose Course 처리부 끝 ------------------------------------------------*/



    /* ----------------------------------- Select Item 처리부 시작 ------------------------------------------------*/
    var item_table = $('#id_dt_select_items').DataTable( {
        paging: false
    } );

    $(document).on("click", "#btn_regstudent_select_items", function(e){
        var ids = [];
        $('input[name="item_pks"]').each(function(){
            ids.push(this.value);
        });

        var ctrl = $(this);
        e.preventDefault();
        item_table.destroy();

        item_table = $('#id_dt_select_items').DataTable( {
            ajax: { 
                "url" : ctrl.attr("ajaxurl"),
                "data": {
                },
            },
            'columnDefs': [{
                'targets': 0,
                'searchable': false,
                'orderable': false,
                'className': 'dt-body-center',
                'render': function (data, type, full, meta){
                    return '<input type="checkbox" name="item_id[]" value="' + $('<div/>').text(data).html() + '">';
                }
             }],
             'order': [[1, 'asc']],
            columns: [
                {"data": "id"},
                {"data": "item_name"},
                {"data": "item_quantity"},
                {"data": "price"}
            ],
            "drawCallback": function(settings){
                item_table.$('input[name="item_id[]"]').each(function(){
                    if (ids.indexOf(this.value) !== -1){
                        $(this).prop("checked", true);
                    }
                });
            }
        });
    });

    $('#th-select-all-items').on('click', function(){
        // Get all rows with search applied
        var rows = item_table.rows({ 'search': 'applied' }).nodes();
        // Check/uncheck checkboxes for all rows in the table
        $('input[type="checkbox"]', rows).prop('checked', this.checked);
    });

    // Handle click on checkbox to set state of "Select all" control
    $('#id_dt_select_items tbody').on('change', 'input[type="checkbox"]', function(){
        // If checkbox is not checked
        if(!this.checked){
           var el = $('#th-select-all-items').get(0);
           // If "Select all" control is checked and has 'indeterminate' property
           if(el && el.checked && ('indeterminate' in el)){
              // Set visual state of "Select all" control
              // as 'indeterminate'
              el.indeterminate = true;
           }
        }
    });

    // 아이템선택모달에서 선택된 아이템들을 메인테이블에 그리기 
    $(document).on('click', '#id-btn-select-item', function(e){
        var item_ids = [];
        e.preventDefault();
        item_table.$('input[name="item_id[]"]').each(function(){
            if(this.checked){
                item_ids.push(this.value);
            }
        });

        $.ajax({
            url: "get_item_list", //선택된 강좌의 primary key값(배렬)들을 가지고 DB에 조회하기
            type: 'post',
            dataType: 'json',
            data : JSON.stringify(item_ids), //자바스크립트 배렬을 JSON형태로 변환하기
            beforeSend: function () {
            },
            success: function (resp) {
                $('#table_purchased_info .tr_items').remove(); //이미전에 추가된 tr 모두 삭제하기 
                
                json_result = JSON.parse(resp);
                for (var i in json_result){
                    var innerHtml =  "<tr class='tr_items'>";
                    innerHtml += '<input type="hidden" name="item_pks" value="' + json_result[i].pk + '">';
                    innerHtml += '<td>' + json_result[i].fields.item_name + '</td>';
                    innerHtml += '<td></td>';
                    innerHtml += '<td><input type="text" value="' + json_result[i].fields.price + '">/' + json_result[i].fields.price_unit + '</td>';
                    innerHtml += '<td><input type="text">' + json_result[i].fields.price_unit + '</td>';
                    innerHtml += '<td>0.00 yuan</td>';
                    innerHtml += '<td></td>';
                    innerHtml += '<td><input type="text"></td>';
                    innerHtml += '</tr>';
                    $('#table_purchased_info > tbody:last').append(innerHtml);
                }
            }
        });
    });
    /* ----------------------------------- Select Item 처리부 끝 ------------------------------------------------*/

    /* ----------------------------------- Choose Fee 처리부 시작 ------------------------------------------------*/
    var fee_table = $('#id_dt_select_fees').DataTable( {
        paging: false
    } );

    $(document).on("click", "#btn_regstudent_select_fees", function(e){
        var ids = [];
        $('input[name="fee_pks"]').each(function(){
            ids.push(this.value);
        });

        var ctrl = $(this);
        e.preventDefault();
        fee_table.destroy();

        fee_table = $('#id_dt_select_fees').DataTable( {
            ajax: { 
                "url" : ctrl.attr("ajaxurl"),
                "data": {
                },
            },
            'columnDefs': [{
                'targets': 0,
                'searchable': false,
                'orderable': false,
                'className': 'dt-body-center',
                'render': function (data, type, full, meta){
                    return '<input type="checkbox" name="fee_id[]" value="' + $('<div/>').text(data).html() + '">';
                }
             }],
             'order': [[1, 'asc']],
            columns: [
                {"data": "id"},
                {"data": "fee_name"},
                {"data": "price"}
            ],
            "drawCallback": function(settings){
                fee_table.$('input[name="fee_id[]"]').each(function(){
                    if (ids.indexOf(this.value) !== -1){
                        $(this).prop("checked", true);
                    }
                });
            }
        });
    });

    $('#th-select-all-fees').on('click', function(){
        // Get all rows with search applied
        var rows = fee_table.rows({ 'search': 'applied' }).nodes();
        // Check/uncheck checkboxes for all rows in the table
        $('input[type="checkbox"]', rows).prop('checked', this.checked);
    });

    // Handle click on checkbox to set state of "Select all" control
    $('#id_dt_select_fees tbody').on('change', 'input[type="checkbox"]', function(){
        // If checkbox is not checked
        if(!this.checked){
           var el = $('#th-select-all-fees').get(0);
           // If "Select all" control is checked and has 'indeterminate' property
           if(el && el.checked && ('indeterminate' in el)){
              // Set visual state of "Select all" control
              // as 'indeterminate'
              el.indeterminate = true;
           }
        }
    });

    // 아이템선택모달에서 선택된 아이템들을 메인테이블에 그리기 
    $(document).on('click', '#id-btn-select-fee', function(e){
        var fee_ids = [];
        e.preventDefault();
        fee_table.$('input[name="fee_id[]"]').each(function(){
            if(this.checked){
                fee_ids.push(this.value);
            }
        });

        $.ajax({
            url: "get_fee_list", //선택된 Fee의 primary key값(배렬)들을 가지고 DB에 조회하기
            type: 'post',
            dataType: 'json',
            data : JSON.stringify(fee_ids), //자바스크립트 배렬을 JSON형태로 변환하기
            beforeSend: function () {
            },
            success: function (resp) {
                $('#table_purchased_info .tr_fees').remove(); //이미전에 추가된 tr 모두 삭제하기 
                
                json_result = JSON.parse(resp);
                for (var i in json_result){
                    var innerHtml =  "<tr class='tr_fees'>";
                    innerHtml += '<input type="hidden" name="fee_pks" value="' + json_result[i].pk + '">';
                    innerHtml += '<td>' + json_result[i].fields.fee_name + '</td>';
                    innerHtml += '<td></td>';
                    innerHtml += '<td><input type="text" value="' + json_result[i].fields.price + '">/' + json_result[i].fields.price_unit + '</td>';
                    innerHtml += '<td><input type="text">' + json_result[i].fields.price_unit + '</td>';
                    innerHtml += '<td>0.00 yuan</td>';
                    innerHtml += '<td></td>';
                    innerHtml += '<td><input type="text"></td>';
                    innerHtml += '</tr>';
                    $('#table_purchased_info > tbody:last').append(innerHtml);
                }
            }
        });
    });
    /* ----------------------------------- Choose Fee 처리부 끝 ------------------------------------------------*/

    //학생등록완료처리부
    $(document).on('click', '#btn_confirm_register', function(e){
        e.preventDefault();
        var purchase_items = [
            {
                'course_id' : 1,
                'pricing_standard_id' : 1,
                'unit_price' : 100,
                'purchase_amount' : 2,
                'gift_days' : 5,
            },
            {
                'course_id' : 2,
                'pricing_standard_id' : 1,
                'unit_price' : 1000,
                'purchase_amount' : 2,
                'gift_days' : 50,
            },
        ];

        var post_data = {
            //First Page Values 'Student Information'
            'name' : $('#id_name').val(),
            'parent_type' : $('#id_parents').text(),
            'parent_phone_no' : $('#id_phoneno').val(),
            'gender' : $('#id_gender').val(),
            'birthday': $('#id_birthday').val(),
            'schoolname' : $('#id_school').val(),
            'grade_no' : $('#id_grade').val(),
            'sourceofstudent_no' : $('#id_source_of_student').val(),
            'alt_parent_type' : $('#id_parents2').text(),
            'alt_parent_phone_no' : $('#id_alt_phoneno').val(),
            'address' : $('#id_homeaddress').val(),

            //Second Page Values 'Purchase Item'
            'purchase_infos' : purchase_items,

            //Third Page Values: 'Billing Message'
            'actual_amount' : $('#id_actual_amount').val(),
            'payment_method' : $('#id_paymentmethod').val(),
            'payment_date' : $('#id_payment_date').val(),
            'manager' : $('#id_manager').val(),
            'follower' : $('#id_follower').val(),
            'remarks' : $('#id_remark').val(),
        };

        $.ajax({
            url: "add_student", 
            type: 'post',
            dataType: 'json',
            data : JSON.stringify(post_data), 
            beforeSend: function () {
            },
            success: function (resp) {
                console.log(resp);
                alert(resp);
            }
        });
    });


    /* ------------------------------------------------------------------------------------------------------------------------------ */
    /* ------------------------------------------Course Fee 처리부--------------------------------------------------- */
    
    /* -------------------------------------------- 1. Item 처리부 ------------------------------------------------------------------- */
    // 아이템을 DB에 추가하기위한 AJAX처리부분
    $(document).on('click', '#id_btn_newitem_add', function(e){
        e.preventDefault();

        var post_data = {
            //First Page Values 'Student Information'
            'item_name' : $('#id_cf_newitem_itemname').val(),
            'unit_price' : $('#id_cf_newitem_unitprice').val(),
            'currency' : 'CNY',
            'stock_amount' : $('#id_cf_newitem_quantity').val(),
            'status' : 1
        };

        $.ajax({
            url: "add_item", 
            type: 'post',
            dataType: 'json',
            data : JSON.stringify(post_data), 
            beforeSend: function () {
            },
            success: function (resp) {
                $('#table_coursefee_itemlist .tr_itemlist').remove();
                var json_result = JSON.parse(resp); //결과로 넘어온 json_string 을 javascript json 오브젝트로 변환하기 
                json_result.forEach(function(item){
                    var innerHtml =  "<tr class='tr_itemlist'>";
                    innerHtml += '<input type="hidden" name="item_pks" value="' + item.pk + '">';
                    innerHtml += '<td>' + item.fields.item_name + '</td>';
                    innerHtml += '<td>' + item.fields.unit_price + '&nbsp;' + item.fields.currency + '</td>';
                    innerHtml += '<td>' + item.fields.stock_amount + '</td>';
                    innerHtml += '<td>Unbound</td>';
                    if (item.fields.status == 1) {
                        innerHtml += '<td>Enabled</td>';
                    }
                    else {
                        innerHtml += '<td>Disabled</td>';
                    }
                    innerHtml += '<td><i class="ti-pencil"><i class="ti-clipboard"></i><i class="ti-trash"></i></td>';
                    innerHtml += '</tr>';
                    $('#table_coursefee_itemlist > tbody:last').append(innerHtml);
                });

                $('#id_btn_newitem_dlg_cancel').click();
                $('.cf_itemdlg').val('');
            }
        });
    });

    //아이템 EditItem Modal 현시하기
    $(document).on('click', '.tr_itemlist .ti-pencil', function(e){
        var item_id = $(this).closest('tr.tr_itemlist').find('input').val();
        
        $('#id_model_article_edititem').modal('show');

        $('#id_cf_edititem_itemid').val(item_id);
        $('#id_cf_edititem_itemname').val($(this).closest('tr.tr_itemlist').find('td').eq(0).html());
        var _tmp = $(this).closest('tr.tr_itemlist').find('td').eq(1).html();
        var _up = _tmp.split('&nbsp;');
        $('#id_cf_edititem_unitprice').val(_up[0]);
        $('#id_cf_edititem_quantity').val($(this).closest('tr.tr_itemlist').find('td').eq(2).html());
    });

    //EditItem에서 수정된 값으로 수정하기 
    $(document).on('click', '#id_btn_edititem_save', function(e){
        var post_data = {
                'item_id' : $('#id_cf_edititem_itemid').val(),
                'item_name' : $('#id_cf_edititem_itemname').val(),
                'item_unitprice' : $('#id_cf_edititem_unitprice').val(),
                'item_quantity' : $('#id_cf_edititem_quantity').val(),
        };
        
        $.ajax({
            url: "edit_item", 
            type: 'post',
            dataType: 'json',
            data : JSON.stringify(post_data), 
            success: function (resp) {
                $('#table_coursefee_itemlist .tr_itemlist').remove();

                var json_result = JSON.parse(resp); //결과로 넘어온 json_string 을 javascript json 오브젝트로 변환하기 
                json_result.forEach(function(item){
                    var innerHtml =  "<tr class='tr_itemlist'>";
                    innerHtml += '<input type="hidden" name="item_pks" value="' + item.pk + '">';
                    innerHtml += '<td>' + item.fields.item_name + '</td>';
                    innerHtml += '<td>' + item.fields.unit_price + '&nbsp;' + item.fields.currency + '</td>';
                    innerHtml += '<td>' + item.fields.stock_amount + '</td>';
                    innerHtml += '<td>Unbound</td>';
                    if (item.fields.status == 1) {
                        innerHtml += '<td>Enabled</td>';
                    }
                    else {
                        innerHtml += '<td>Disabled</td>';
                    }
                    innerHtml += '<td><i class="ti-pencil"></i><i class="ti-clipboard"></i><i class="ti-trash"></i></td>';
                    innerHtml += '</tr>';
                    $('#table_coursefee_itemlist > tbody:last').append(innerHtml);
                });

                $('#id_model_article_edititem').modal('hide');
            }
        });
    });
    

    //현재 선택된 테이블row삭제하고 해당 item을 DB에서 지우도록 ajax 요청하기
    $(document).on('click', '.tr_itemlist .ti-trash', function(e){
        var item_id = $(this).closest('tr.tr_itemlist').find('input').val();
        var current_row = $(this).closest('tr.tr_itemlist');

        var post_data = {
            'item_id': item_id
        };
        $.ajax({
            url: "delete_item", 
            type: 'post',
            dataType: 'json',
            data : JSON.stringify(post_data), 
            beforeSend: function () {
            },
            success: function (resp) {
                current_row.remove();
                console.log(resp);
            }
        });
    });

    /* -------------------------------------------- 2. Fee 처리부 ------------------------------------------------------------------- */

    // Fee를 DB에 추가하기위한 AJAX처리부분
    $(document).on('click', '#id_btn_newfee_add', function(e){
        e.preventDefault();

        var post_data = {
            //First Page Values 'Student Information'
            'fee_name' : $('#id_cf_newfee_feename').val(),
            'unit_price' : $('#id_cf_newfee_unitprice').val(),
            'currency' : 'CNY',
            'status' : 1
        };

        $.ajax({
            url: "add_fee", 
            type: 'post',
            dataType: 'json',
            data : JSON.stringify(post_data), 
            success: function (resp) {
                $('#table_coursefee_feelist .tr_feelist').remove();
                var json_result = JSON.parse(resp); //결과로 넘어온 json_string 을 javascript json 오브젝트로 변환하기 
                json_result.forEach(function(fee){
                    var innerHtml =  "<tr class='tr_feelist'>";
                    innerHtml += '<input type="hidden" name="fee_pks" value="' + fee.pk + '">';
                    innerHtml += '<td>' + fee.fields.fee_name + '</td>';
                    innerHtml += '<td>' + fee.fields.unit_price + '</td>';
                    innerHtml += '<td>Unbound</td>';
                    if (fee.fields.status == 1) {
                        innerHtml += '<td>Enabled</td>';
                    }
                    else {
                        innerHtml += '<td>Disabled</td>';
                    }
                    innerHtml += '<td><i class="ti-pencil mr-4"></i><i class="ti-trash"></i></td>';
                    innerHtml += '</tr>';
                    $('#table_coursefee_feelist > tbody:last').append(innerHtml);
                });

                $('#id_btn_newfee_dlg_cancel').click();
                $('.cf_feedlg').val('');
            }
        });
    });

    //현재 선택된 테이블row삭제하고 해당 Fee을 DB에서 지우도록 ajax 요청하기
    $(document).on('click', '.tr_feelist .ti-trash', function(e){
        var fee_id = $(this).closest('tr.tr_feelist').find('input').val();
        var current_row = $(this).closest('tr.tr_feelist');

        var post_data = {
            'fee_id': fee_id
        };
        $.ajax({
            url: "delete_fee", 
            type: 'post',
            dataType: 'json',
            data : JSON.stringify(post_data), 
            beforeSend: function () {
            },
            success: function (resp) {
                current_row.remove();
                console.log(resp);
            }
        });
    });

    //아이템 EditFee Modal 현시하기
    $(document).on('click', '.tr_feelist .ti-pencil', function(e){
        var item_id = $(this).closest('tr.tr_feelist').find('input').val();
        
        $('#id_model_article_editfee').modal('show');

        $('#id_cf_editfee_feeid').val(item_id);
        $('#id_cf_editfee_feename').val($(this).closest('tr.tr_feelist').find('td').eq(0).html());
        var _tmp = $(this).closest('tr.tr_feelist').find('td').eq(1).html();
        var _up = _tmp.split('&nbsp;');
        $('#id_cf_editfee_unitprice').val(_up[0]);
    });

    //EditFee에서 수정된 값으로 수정하기 
    $(document).on('click', '#id_btn_editfee_save', function(e){
        var post_data = {
                'fee_id' : $('#id_cf_editfee_feeid').val(),
                'fee_name' : $('#id_cf_editfee_feename').val(),
                'fee_unitprice' : $('#id_cf_editfee_unitprice').val(),
        };
        
        $.ajax({
            url: "edit_fee", 
            type: 'post',
            dataType: 'json',
            data : JSON.stringify(post_data), 
            success: function (resp) {
                $('#table_coursefee_feelist .tr_feelist').remove();

                var json_result = JSON.parse(resp); //결과로 넘어온 json_string 을 javascript json 오브젝트로 변환하기 
                json_result.forEach(function(fee){
                    var innerHtml =  "<tr class='tr_feelist'>";
                    innerHtml += '<input type="hidden" name="fee_pks" value="' + fee.pk + '">';
                    innerHtml += '<td>' + fee.fields.fee_name + '</td>';
                    innerHtml += '<td>' + fee.fields.unit_price + '&nbsp;' + fee.fields.currency + '</td>';
                    innerHtml += '<td>Unbound</td>';
                    if (fee.fields.status == 1) {
                        innerHtml += '<td>Enabled</td>';
                    }
                    else {
                        innerHtml += '<td>Disabled</td>';
                    }
                    innerHtml += '<td><i class="ti-pencil mr-4"></i><i class="ti-trash"></i></td>';
                    innerHtml += '</tr>';
                    $('#table_coursefee_feelist > tbody:last').append(innerHtml);
                });

                $('#id_model_article_editfee').modal('hide');
            }
        });
    });

    /* -------------------------------------------- 3. Course 처리부 ------------------------------------------------------------------- */
    $(document).on('click', '#btn_coursefee_edit_cancel', function(e){
        e.preventDefault();
        location.href = 'coursesfee';
    });
});

