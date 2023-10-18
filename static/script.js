$(document).ready(function() {
    // Populate teacher and student dropdowns
    $.get('/teachers', function(data) {
        for (var i = 0; i < data.teachers.length; i++) {
            $('#teacher').append($('<option>', {
                value: data.teachers[i].teacher_id,
                text: data.teachers[i].teacher_name
            }));
        }
    });

    $.get('/students', function(data) {
        for (var i = 0; i < data.students.length; i++) {
            $('#student').append($('<option>', {
                value: data.students[i].student_id,
                text: data.students[i].student_name
            }));
        }
    });

    // Associate student and teacher
    $('#associate-button').click(function() {
        var teacherId = $('#teacher').val();
        var studentId = $('#student').val();
        $.post('/associate', { teacher_id: teacherId, student_id: studentId }, function(data) {
            alert(data);
        });
    });

    // Generate certificate
    $('#generate-certificate-button').click(function() {
        var teacherId = $('#teacher').val();
        var studentId = $('#student').val();
        $.post('/generate_certificate', { teacher_id: teacherId, student_id: studentId }, function(data) {
            $('#certificate-result').html(data);
        });
    });
});
