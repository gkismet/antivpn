// Copy buttons on code blocks
document.querySelectorAll('pre').forEach(function (pre) {
  var btn = document.createElement('button');
  btn.className = 'copy-btn';
  btn.type = 'button';
  btn.textContent = '复制';
  btn.addEventListener('click', function () {
    var text = pre.querySelector('code') ? pre.querySelector('code').innerText : pre.innerText;
    var done = function () { btn.textContent = '已复制 ✓'; setTimeout(function () { btn.textContent = '复制'; }, 1500); };
    if (navigator.clipboard) { navigator.clipboard.writeText(text).then(done, function () {}); }
  });
  pre.appendChild(btn);
});

// Stock tables: <div data-stock="cg,ntt,gtt"></div>
var STOCK_LABEL = { ok: '有货', low: '库存极少', out: '售罄' };
function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

var holders = document.querySelectorAll('[data-stock]');
if (holders.length) {
  fetch('stock.json', { cache: 'no-cache' })
    .then(function (r) { return r.json(); })
    .then(function (data) {
      document.querySelectorAll('[data-stock-updated]').forEach(function (el) { el.textContent = data.updated; });
      holders.forEach(function (holder) {
        var ids = holder.getAttribute('data-stock').split(',');
        var html = '';
        data.lines.filter(function (l) { return ids.indexOf(l.id) !== -1; }).forEach(function (line) {
          html += '<h3>' + esc(line.name) + (line.china ? '' : ' <span class="badge">无中国大陆优化</span>') + '</h3>';
          html += '<div class="table-wrap"><table><thead><tr><th>套餐</th><th>配置</th><th>月付（CAD）</th><th>库存</th><th></th></tr></thead><tbody>';
          line.plans.forEach(function (p) {
            html += '<tr><td><strong>' + esc(p.name) + '</strong></td><td>' + esc(p.spec) + '</td>' +
              '<td class="price">' + esc(p.price) + ' <span class="muted">' + esc(p.cny) + '</span></td>' +
              '<td class="stock ' + esc(p.stock) + '">' + STOCK_LABEL[p.stock] + '</td>' +
              '<td><a href="' + esc(data.aff) + '" rel="sponsored noopener" target="_blank">' + (p.stock === 'out' ? '预订补货' : '去购买') + ' →</a></td></tr>';
          });
          html += '</tbody></table></div>';
        });
        holder.innerHTML = html;
      });
    })
    .catch(function () {
      holders.forEach(function (h) { h.innerHTML = '<p class="muted">库存数据加载失败，请直接查看 <a href="https://novixlink.com/aff.php?aff=580" rel="sponsored noopener">NovixLink 官网</a>。</p>'; });
    });
}
