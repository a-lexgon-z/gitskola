

document.querySelectorAll('.videoPreview').forEach(function(vid) {
  vid.onmouseover = function() {
    this.play();
  }
  vid.onmouseout = function() {
    this.load(); // stop and show poster
  }
})