
function attachLinkToClipboard() {
    const linkInput = document.getElementById('link-input');
    const value = linkInput.value;
    navigator.clipboard.writeText(value);
    markTextAttached();
}

function markTextAttached() {
    const copyButton = document.getElementById('copy-link');
    copyButton.innerText = "Copied!";
}