$(document).ready(function() {

    $("#postForm").on("submit", function(event) {
      event.preventDefault();
      console.log("WHAT");
      $.ajax({
          data : {
            first_name : $("#post_fname").val().trim(),
            last_name : $("#post_lname").val().trim(),
            salary : $("#post_salary").val().trim(),
            address : $("#post_address").val().trim(),
            date_hired : $("#post_dhired").val().trim(),
          },
          type : "POST",
          url : '/api/employee_records',
      }).done(function(data) {
          console.log(data);
          var form = $("#postForm");
          messageBoxHandler(data, form);
      });
    });

    $("#deleteForm").on("submit", function(event) {
      event.preventDefault();
      console.log("ISSA DEELET");

      // endpoint handler, name or id
      var id = $("#del_id").val().trim();
      var full_name = $("#del_name").val().trim();
      full_name.replace(" ","_")

      if (id == '' && full_name == '') {
          // add the error class to the input boxes
          console.log("EMPTY INPUTS ERROR");
          return
      } else if (id != '') {
          var endpoint = id;
      } else if (full_name != '') {
          var endpoint = full_name;
      }

      $.ajax({
          data : {
            id : id,
            full_name : full_name,
          },
          type : "DELETE",
          url : '/api/employee_records/' + endpoint,
      }).done(function(data) {
          console.log(data);
          var form = $("#deleteForm");
          messageBoxHandler(data, form);
      });
    });

    $("#getForm").on("submit", function(event) {
        event.preventDefault();

        var id = $("#get_id").val().trim();
        var name = $("#get_name").val().trim();

        if (id == '' && name == '') {
            console.log("WE HAVE THE RETURN A ERROR");
        } else if (id != '') {
            window.location.href = '/api/employee_records/' + id;
        } else if (name != '') {
            name = name.replace(" ","_");
            window.location.href = '/api/employee_records/' + name;
        }
    });

    $("#putForm").on("submit", function(event) {
        event.preventDefault();
        console.log("PUTTTT FORM");

        // Add the validation for these inputs
        var id = $("#put_id").val().trim();
        var first_name = $("#put_fname").val().trim();
        var last_name = $("#put_lname").val().trim();
        var address = $("#put_address").val().trim();
        var salary = $("#put_salary").val().trim();
        var date_hired = $("#put_dhired").val().trim();

        $.ajax({
            data : {
              id : id,
              first_name : first_name,
              last_name : last_name,
              address : address,
              salary : salary,
              date_hired : date_hired,
            },
            type : "PUT",
            url : '/api/employee_records/' + id,
        }).done(function(data) {
            console.log(data);
            var form = $("#putForm");
            messageBoxHandler(data, form);
        });
    })

    function messageBoxHandler(data, form) {
      console.log("WILL THSI WORK?");
      if (data.error) {
        console.log("IN THE ERROR");
        form.find(".messageBox").css("display","block");
        form.find(".messageBox").removeClass("successBox");
        form.find(".messageBox").addClass("errorBox");
        form.find(".result").html("Error");
        form.find(".message").html(data.error);
      } else if (data.success) {
        console.log("IN THE SUCCESS");
        form.find(".messageBox").css("display","block");
        form.find(".messageBox").removeClass("errorBox");
        form.find(".messageBox").addClass("successBox");
        form.find(".result").html("Success");
        form.find(".message").html(data.success);
      }
      setTimeout(function() {
        form.find(".messageBox").css("display","none");
      }, 5000);
    }
});

function expandForm(div) {
    console.log("ISSA FUCKIN LOIOOOOOOOOOT");
    var form = div.nextElementSibling;
    form.style.display == "none" ? form.style.display = "block" : form.style.display = "none";
    console.log(form);
}

function getInputHandler(btn) {
    console.log("HEY MANE");
    var formDiv = btn.closest(".form-div");
    var formInputs = formDiv.querySelectorAll("input")
    console.log("YEET");
    console.log(formInputs);
    var id = formInputs[0].value.trim();
    var name = formInputs[1].value.trim();

    console.log(id);
    console.log(name);

    if (id == '' && name == '') {
      console.log("EMPTY ASS SHIT WE GONE ERROR THIS B");
    } else if (id != '') {
      console.log("WE GONA SEND THE ID IN HEERERE");
      window.location.href = '/api/employee_records/' + id;
    } else if (name != '') {
      console.log("WE SENDING THSI SHIT SDJFKDFGJD WTIH THE NAME");
      name = name.replace(" ","_");
      console.log(name);
      window.location.href = '/api/employee_records/' + name;
    }

    // window.location.href = '/api/employee_records';
}

function postInputHandler(btn) {
  console.log("HEY POOP");
  var formDiv = btn.closest(".form-div");
  var formInputs = formDiv.querySelectorAll("input")
  var valid = true;

  for (let input of formInputs) {
    if (input.value.trim() == "") {
      console.log("make this things error box red");
      valid = false;
    }
  }

  if (valid) {
    var firstName = formInputs[0].value.trim();
    var lastName = formInputs[1].value.trim();
    var address = formInputs[2].value.trim();
    var salary = formInputs[3].value.trim();
    var dateHired = formInputs[4].value.trim();
  } else {
    return
  }

  json_data = {
    first_name : firstName,
    last_name : lastName,
    address : address,
    salary : salary,
    date_hired : dateHired,
  }

  console.log(json_data);
}

function allEmployeeData() {
    window.location.href = '/api/employee_records';
}
