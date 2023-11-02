$("#user_input_form").on("submit", function (e) {
    e.preventDefault();
    motionName = document.getElementById("motion_select").value;
    var model = new LAppModel();
    model.startAppointMotion(motionName, 3, 0);
});
