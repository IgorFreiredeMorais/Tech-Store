$(document).ready(function () {
  searchButton = $(".search-button");
  searchForm = $("search-form");

  $(searchButton).on("click", function () {
    searchForm.submit();
  });
});
