 <script type="text/javascript">
 	function setIframeHeight(iframe) {
if (iframe) {
var iframeWin = iframe.contentWindow || iframe.contentDocument.parentWindow;
if (iframeWin.document.body) {
iframe.height = iframeWin.document.documentElement.scrollHeight || iframeWin.document.body.scrollHeight;
}
}
};
window.onload = function () {
setIframeHeight(document.getElementById('external-frame'));
};
 </script>

<iframe src ="//bcb.unl.edu/dbpup_download/" frameborder="0" scrolling="no" id="external-frame" onload="setIframeHeight(this)" style="width:100%;"></iframe>