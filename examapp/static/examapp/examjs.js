jQuery(document).ready(function(){
    $('.datepicker').datepicker(
        {
        'dateFormat': 'yy-mm-dd', 
        changeMonth: true,
        changeYear: true
         }   
    );
jQuery('.select2').select2()
jQuery('#id_ExamDate').change(function(e){
e.preventDefault()
    
var value=jQuery('#id_ExamDate').val()
// alert(value.substring(0,4))
var yearpart=value.substring(0,4)
jQuery('#id_ExamYear').val(yearpart)
})

jQuery('#id_ExamDuration').change(function(e){
e.preventDefault()
tym=jQuery('#id_ExamDuration').val()
if (tym > 5) 
{
    alert("Exan duration cant be greater than 5")
}
})
jQuery('#drpsubject').change(function () {
    var examtype = jQuery('#drpexamtype').val()
    var subjectid = jQuery(this).val()
    // alert(examtype)
    jQuery.ajax({

      type: "GET",
      url: "/getquestions",
      data: {
        type: examtype,
        subject: subjectid
      },
      success: function (data) {
        jQuery('#drpquestions').empty()
               
        $.each(data, function (i, item) {
                console.log(i)
                console.log(item) 
                var optionstring="" 
                optionstring=`<option value=${i}>${item}</option>`
                jQuery('#drpquestions').append(optionstring)
        });
               
       
     }
    })
})

jQuery('#drpexamtype').change(function () {
  var subjectid = jQuery('#drpsubject').val()
  var examtypeid= jQuery(this).val()
  // alert(examtype)
  jQuery.ajax({

    type: "GET",
    url: "/getquestions",
    data: {
      type: examtypeid,
      subject: subjectid
    },
    success: function (data) {
      jQuery('#drpquestions').empty()
             
      $.each(data, function (i, item) {
              console.log(i)
              console.log(item)  
              var optionstring="" 
                optionstring=`<option value=${i}>${item}</option>`
                jQuery('#drpquestions').append(optionstring)
      });
             
     
   }
  })
})

jQuery('#btnshowqns').click(function(){

  

  var examid = jQuery('#drpexam').val()
  var subjectid = jQuery('#drpsubject').val()
  var examtypeid = jQuery('#drpexamtypenew').val()
  
  jQuery.ajax({

    type: "GET",
    url: "/showquestions",
    data: {
      examtype: examtypeid,
      subject: subjectid,
      exam : examid,
    },
    success: function (data) {
      var ullist = jQuery('#ulQuestionlist')
      ullist.html("");
      $.each(data, function (i, item) {
      console.log('hello')
              console.log(i)
              console.log(item) 
              console.log(data) 
              if(i=='existing'){
                $.each(item, function (j, myitem) {
      var optionstring=`<li><div  style='border:2px solid orange;display:flex;margin-bottom:5px'><div> 
           <input type='checkbox' style= 'width:30px;height:30px;margin-right:30px;margin-left:30px' checked value=${j} class='chkqn' name='sanjeev' /> </div>
              
                  <div style='margin-right:20px;margin-left:20px;font-size:20px'> ${myitem}</div></div></li>`
                  ullist.append(optionstring)
                   })
               }
              if(i=='remaining'){
                $.each(item, function (j, myitem) {
      var optionstring=`<li><div  style='border:2px solid orange;display:flex;margin-bottom:5px'><div> 
           <input type='checkbox' style= 'width:30px;height:30px;margin-right:30px;margin-left:30px' value=${j} class='chkqn' name='sanjeev' /> </div>
              
                  <div style='margin-right:20px;margin-left:20px;font-size:20px'> ${myitem}</div></div></li>`
                  ullist.append(optionstring)
                   })
               }
            //   var optionstring=`<li><div  style='border:2px solid orange;display:flex;margin-bottom:5px'><div> 
            //   <input type='checkbox' style= 'width:30px;height:30px;margin-right:30px;margin-left:30px' value=${i} class='chkqn' name='sanjeev' /> </div>
              
            //  <div style='margin-right:20px;margin-left:20px;font-size:20px'> ${item}</div></div></li>`
            //   ullist.append(optionstring)

      });
      var chklist=document.getElementsByClassName('.chkqn')
      chklist.forEach(function(checkbox) {
        checkbox.addEventListener('checked', function() {
          alert('hello')
        })
      })
    }
  })
})
})

