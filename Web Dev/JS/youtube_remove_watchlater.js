var watchLaterButton = $('body').getElementsByClassName("yt-uix-button yt-uix-button-size-default yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup pl-video-edit-remove yt-uix-tooltip");
var loadButton = $('body').getElementsByClassName("yt-uix-button yt-uix-button-size-default yt-uix-button-default load-more-button yt-uix-load-more browse-items-load-more-button");
var videos = prompt("How much videos ?");
var loadTime= Math.floor(videos/100);
function loadVideos(){
    setInterval(function () {
        loadButton[0].click();
    },500);
};
function deleteWatchLater(i) {
    setInterval(function () {
        watchLaterButton[i].click();
    }, 500);
};
for (var j = 0; j < loadTime; ++j){
    loadVideos();
};
for (var i = 0; i < videos; ++i){
    deleteWatchLater(i);
};
