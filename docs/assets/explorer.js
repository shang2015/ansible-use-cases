// Module Explorer: filter every module/role/plugin across all collections.
(function () {
  function init() {
    var root = document.getElementById("uc-explorer");
    if (!root || root.dataset.ready) return;
    root.dataset.ready = "1";
    var base = root.dataset.base || "";
    var q = root.querySelector("#uc-q"),
      fType = root.querySelector("#uc-type"),
      fSupport = root.querySelector("#uc-support"),
      fDomain = root.querySelector("#uc-domain"),
      fDep = root.querySelector("#uc-dep"),
      count = root.querySelector("#uc-count"),
      body = root.querySelector("#uc-body"),
      more = root.querySelector("#uc-more");
    var data = [], shown = 200;
    var typeLabel = {
      module: "Module", role: "Role", playbook: "Playbook", inventory: "Inventory",
      lookup: "Lookup", filter: "Filter", test: "Test", eda_event_source: "EDA source",
      eda_event_filter: "EDA filter", connection: "Connection", callback: "Callback", action: "Action"
    };
    function opts(sel, values, label) {
      values.sort().forEach(function (v) {
        var o = document.createElement("option");
        o.value = v; o.textContent = label ? label(v) : v;
        sel.appendChild(o);
      });
    }
    function anchor(name) { return name.replace(/\./g, "").replace(/_/g, "-").toLowerCase(); }
    function esc(s) {
      return String(s).replace(/[&<>"]/g, function (c) {
        return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
      });
    }
    function render() {
      var terms = q.value.toLowerCase().split(/\s+/).filter(Boolean);
      var t = fType.value, s = fSupport.value, m = fDomain.value, hideDep = fDep.checked;
      var rows = data.filter(function (r) {
        if (t && r.t !== t) return false;
        if (s && r.s !== s) return false;
        if (m && r.m !== m) return false;
        if (hideDep && r.x) return false;
        if (!terms.length) return true;
        var hay = (r.n + " " + r.d).toLowerCase();
        return terms.every(function (w) { return hay.indexOf(w) !== -1; });
      });
      count.textContent = rows.length.toLocaleString() + " of " + data.length.toLocaleString() + " items";
      var html = rows.slice(0, shown).map(function (r) {
        var short = r.n.slice(r.c.length + 1);
        return "<tr><td><a href=\"" + base + "collections/" + r.c + "/#" + anchor(short) + "\"><code>" + esc(r.n) +
          "</code></a></td><td>" + esc(typeLabel[r.t] || r.t) + "</td><td>" + (r.x ? "<span class=\"uc-badge uc-deprecated\">Deprecated</span> " : "") +
          esc(r.d || "—") + "</td><td>" + esc(r.s) + "</td></tr>";
      }).join("");
      body.innerHTML = html || "<tr><td colspan=4>No matches.</td></tr>";
      more.style.display = rows.length > shown ? "" : "none";
    }
    fetch(base + "assets/content-index.json").then(function (r) { return r.json(); }).then(function (d) {
      data = d;
      var uniq = function (k) { return Object.keys(d.reduce(function (a, r) { a[r[k]] = 1; return a; }, {})); };
      opts(fType, uniq("t"), function (v) { return typeLabel[v] || v; });
      opts(fSupport, uniq("s"));
      opts(fDomain, uniq("m"));
      var params = new URLSearchParams(location.search);
      if (params.get("find")) q.value = params.get("find");
      render();
    });
    [q, fType, fSupport, fDomain, fDep].forEach(function (el) {
      el.addEventListener("input", function () { shown = 200; render(); });
    });
    more.addEventListener("click", function () { shown += 500; render(); });
  }
  if (window.document$) { window.document$.subscribe(init); } else { document.addEventListener("DOMContentLoaded", init); }
})();
