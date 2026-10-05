(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  // Mobile navigation
  var toggle = $('.nav-toggle');
  var nav = $('#site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  // Highlight today in the hours tables (restaurant is in Ontario)
  var today = new Date().toLocaleDateString('en-US', { weekday: 'long', timeZone: 'America/Toronto' });
  $$('tr[data-day]').forEach(function (row) {
    if (row.getAttribute('data-day') === today) row.classList.add('today');
  });

  // Menu: search and category highlight
  var search = $('#menu-search');
  if (search) {
    var cats = $$('.cat');
    var items = $$('.cat .item');
    var none = $('.no-results');
    var run = function () {
      var q = search.value.trim().toLowerCase();
      var shown = 0;
      items.forEach(function (it) {
        var hit = !q || it.textContent.toLowerCase().indexOf(q) !== -1;
        it.classList.toggle('is-hidden', !hit);
        if (hit) shown++;
      });
      $$('.group').forEach(function (g) {
        g.classList.toggle('is-hidden', !g.querySelector('.item:not(.is-hidden)'));
      });
      cats.forEach(function (c) {
        c.classList.toggle('is-hidden', !c.querySelector('.item:not(.is-hidden)'));
      });
      if (none) none.hidden = shown !== 0;
    };
    search.addEventListener('input', run);

    var chips = $$('.chips a');
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) {
            chips.forEach(function (c) {
              var on = c.getAttribute('href') === '#' + en.target.id;
              c.classList.toggle('active', on);
              if (on) {
                var box = c.parentElement;
                box.scrollTo({ left: c.offsetLeft - 24, behavior: 'smooth' });
              }
            });
          }
        });
      }, { rootMargin: '-140px 0px -65% 0px' });
      cats.forEach(function (c) { io.observe(c); });
    }
  }

  // Gallery lightbox
  var gallery = $('#gallery');
  var box = $('#lightbox');
  if (gallery && box && typeof box.showModal === 'function') {
    var shots = $$('.g-item', gallery);
    var idx = 0;
    var big = $('img', box);
    var show = function (i) {
      idx = (i + shots.length) % shots.length;
      big.src = shots[idx].getAttribute('data-full');
      big.alt = $('img', shots[idx]).alt;
    };
    shots.forEach(function (b, i) {
      b.addEventListener('click', function () { show(i); box.showModal(); });
    });
    $('.lb-close', box).addEventListener('click', function () { box.close(); });
    $('.lb-prev', box).addEventListener('click', function () { show(idx - 1); });
    $('.lb-next', box).addEventListener('click', function () { show(idx + 1); });
    box.addEventListener('click', function (e) { if (e.target === box) box.close(); });
    box.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') show(idx - 1);
      if (e.key === 'ArrowRight') show(idx + 1);
    });
  }

  // Forms open the visitor's email app with the details filled in
  $$('form[data-mailto]').forEach(function (form) {
    var status = $('.form-status', form);
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      var lines = [];
      Array.prototype.forEach.call(form.elements, function (f) {
        if (!f.name || !f.value) return;
        var label = f.labels && f.labels[0] ? f.labels[0].firstChild.textContent.trim() : f.name;
        lines.push(label + ': ' + f.value);
      });
      var to = form.getAttribute('data-mailto');
      var subject = form.getAttribute('data-subject');
      window.location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
      if (status) status.textContent = 'Your email app should open with your details filled in. If it does not, email ' + to + ' or call 647.400.0488.';
    });
  });
})();
