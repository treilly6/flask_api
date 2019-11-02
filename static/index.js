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
      })
      .done(function(data) {
          console.log(data);
      });
    });

    $("#deleteForm").on("submit", function(event) {
      event.preventDefault();
      console.log("ISSA DEELET");

      // endpoint handler, name or id

      $.ajax({
          data : {
            id : $("#del_id").val().trim(),
            full_name : $("#del_name").val().trim(),
          },
          type : "DELETE",
          url : '/api/employee_records/',
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

        $.ajax({
            data : {
                poop : "yes",
            },
            type : "PUT",
            url : '/api/employee_records/55',
        });
    })

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
