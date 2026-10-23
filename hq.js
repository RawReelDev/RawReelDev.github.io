// RawReel backup HQ: More menu (close on outside click / Escape) and the quick theme toggle.
// Same behavior as the main site's nav.js, without re-rendering the nav (links here point to the main site).
(function () {
  var menus = document.querySelectorAll('details.more');
  document.addEventListener('click', function (e) {
    menus.forEach(function (d) { if (d.open && !d.contains(e.target)) d.open = false; });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    menus.forEach(function (d) { if (d.open) { d.open = false; d.querySelector('summary').focus(); } });
  });
  document.querySelectorAll('.rr-theme-toggle').forEach(function (b) {
    b.addEventListener('click', function (e) { e.stopPropagation(); if (window.RRS) RRS.cycleTheme(); });
  });
  if (window.RRS) RRS.apply();
})();
