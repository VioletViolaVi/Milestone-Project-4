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

  // stripe elements
  let stripe_public_key = $("#id_stripe_public_key").text().slice(1, -1);
  let client_secret = $("#id_client_secret").text().slice(1, -1);
  let stripe = Stripe(stripe_public_key);
  let elements = stripe.elements();
  let style = {
    base: {
      color: "#212529",
      fontFamily: "sans-serif",
      src: "local('Montserrat Regular'), local('Montserrat-Regular'), url(https://fonts.gstatic.com/s/montserrat/v15/JTUSjIg1_i6t8kCHKm459WRhyyTh89ZNpQ.woff2) format('woff2')",//delete if not used
      fontSmoothing: "antialiased",
      fontSize: "16px",
      "::placeholder": {
        color: "#495057",
      },
    },
    invalid: {
      color: "red",
      iconColor: "red",
    },
  };
  let card = elements.create("card", { style: style });
  card.mount("#stripeCard");
});
