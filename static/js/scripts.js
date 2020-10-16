$(document).ready(function () {
  // smooth scroll to screen top using arrow
  $(".back-to-top-link").click(function () {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });

  // shows or hides back to top arrow
  $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
      $(".fixed-arrow").show();
    } else {
      $(".fixed-arrow").hide();
    }
  });

  // to update drink quantity
  $(".edit-btn").click(function () {
    let editForm = $(this).parent();
    editForm.submit();
  });

//   // to delete drinks
//   $(".bin-btn").click(function () { 
//     let csrfToken = "{{ csrf_token }}";
//     let itemId = $(".delete-modal").attr("id").split("delete_")[1];
//     let url = `/shopping_cart/edit/${itemId}/`;
//     let data = { "csrfmiddlewaretoken": csrfToken };

//     $.post(url, data).done(function () {
//       location.reload();
//     });
//   });
});
