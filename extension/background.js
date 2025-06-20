chrome.action.onClicked.addListener((tab) => {
  if (!tab.url || !tab.url.includes('screener.in')) {
    return;
  }
  chrome.scripting.executeScript({
    target: {tabId: tab.id},
    func: () => ({
      html: document.documentElement.outerHTML,
      title: document.title
    })
  }).then(([{result}]) => {
    const safeTitle = result.title.replace(/[^a-z0-9]+/gi, '_').substring(0, 60);
    const url = 'data:text/html;charset=utf-8,' + encodeURIComponent(result.html);
    chrome.downloads.download({
      url,
      filename: safeTitle + '.html'
    });
  });
});
