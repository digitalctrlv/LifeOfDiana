
// ----------------------------- //
// YOUTUBE PLAYER  
function onYouTubeIframeAPIReady() {
    var onPlayerReady = function(event) {
        // Remove the playVideo() call
        // event.target.playVideo();
        console.log('Player is ready');
    };

    // Initialize YouTube Player
    var player = new YT.Player('player', {
        height: 544,
        width: 760,
        videoId : 'I0__QzksN8w',
        events : {
            'onReady' : onPlayerReady
        }
    });
}
// ----------------------------- //


// ----------------------------- //
// DOWNLOAD DOCUMENTS
function downloadFile(filePath) {
    var element = document.createElement('a');
    element.setAttribute('href', filePath);
    element.setAttribute('download', '');

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}

// Add event listeners to all buttons with the class "download-btn"
document.querySelectorAll(".download-btn").forEach(button => {
    button.addEventListener("click", function () {
        var filePath = this.getAttribute("data-file");
        downloadFile(filePath);
    });
});
// ----------------------------- //


// ----------------------------- //
// IMAGE CLICK AND POP UP
let currentZoom = 1;
let isDragging = false;
let startX, startY, translateX = 0, translateY = 0;

document.addEventListener('DOMContentLoaded', function() {
    const zoomableImages = document.querySelectorAll('.zoomable-image');
    zoomableImages.forEach(img => {
        img.addEventListener('click', function() {
            openModal(this);
        });
    });

    document.getElementById('imageModal').addEventListener('click', function(e) {
        if (e.target === this) {
            closeModal();
        }
    });

    document.addEventListener('keydown', function(e) {
        if (document.getElementById('imageModal').style.display === 'block') {
            if (e.key === 'Escape') {
                closeModal();
            } else if (e.key === '+' || e.key === '=') {
                zoomIn();
            } else if (e.key === '-') {
                zoomOut();
            } else if (e.key === '0') {
                resetZoom();
            }
        }
    });
});

function openModal(img) {
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImage');
    
    modal.style.display = 'block';
    modalImg.src = img.dataset.zoomSrc || img.src;
    modalImg.alt = img.alt;
    
    currentZoom = 1;
    translateX = 0;
    translateY = 0;
    updateImageTransform();
    
    addDragFunctionality(modalImg);
}

function closeModal() {
    document.getElementById('imageModal').style.display = 'none';
}

function zoomIn() {
    currentZoom = Math.min(currentZoom * 1.2, 5);
    updateImageTransform();
}

function zoomOut() {
    currentZoom = Math.max(currentZoom / 1.2, 0.5);
    updateImageTransform();
}

function resetZoom() {
    currentZoom = 1;
    translateX = 0;
    translateY = 0;
    updateImageTransform();
}

function updateImageTransform() {
    const modalImg = document.getElementById('modalImage');
    modalImg.style.transform = `translate(-50%, -50%) translate(${translateX}px, ${translateY}px) scale(${currentZoom})`;
}

function addDragFunctionality(img) {
    img.addEventListener('mousedown', startDrag);
    img.addEventListener('mousemove', drag);
    img.addEventListener('mouseup', endDrag);
    img.addEventListener('mouseleave', endDrag);
    
    // Touch events for mobile
    img.addEventListener('touchstart', startDrag);
    img.addEventListener('touchmove', drag);
    img.addEventListener('touchend', endDrag);
}

function startDrag(e) {
    if (currentZoom > 1) {
        isDragging = true;
        const clientX = e.clientX || e.touches[0].clientX;
        const clientY = e.clientY || e.touches[0].clientY;
        startX = clientX - translateX;
        startY = clientY - translateY;
        e.preventDefault();
    }
}

function drag(e) {
    if (isDragging && currentZoom > 1) {
        const clientX = e.clientX || e.touches[0].clientX;
        const clientY = e.clientY || e.touches[0].clientY;
        translateX = clientX - startX;
        translateY = clientY - startY;
        updateImageTransform();
        e.preventDefault();
    }
}

function endDrag() {
    isDragging = false;
}

// Mouse wheel zoom
document.getElementById('modalImage').addEventListener('wheel', function(e) {
    e.preventDefault();
    if (e.deltaY < 0) {
        zoomIn();
    } else {
        zoomOut();
    }
});
// ----------------------------- //


// ----------------------------- //
// SCROLLING EVENTS AND ARCHIVE CARDS

// Fade hero image on scroll
window.addEventListener('scroll', function() {
    const heroSection = document.getElementById('hero');
    const scrollPosition = window.scrollY;

    // Calculate opacity based on scroll position
    const opacity = 1 - (scrollPosition / 500);

    // Apply opacity if it's between 0 and 1
    if (opacity >= 0 && opacity <= 1) {
        heroSection.style.opacity = opacity;
    }
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);

        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 70,
                behavior: 'smooth'
            });
        }
    });
});

(function() {
    function injectScript() {
        var iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
        if (iframeDoc) {
            var script = iframeDoc.createElement('script');
            script.innerHTML = "window.__CF$cv$params={r:'9542fdeac0541498',t:'MTc1MDY3MTI5MC4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";
            iframeDoc.getElementsByTagName('head')[0].appendChild(script);
        }
    }

    if (document.body) {
        var iframe = document.createElement('iframe');
        iframe.height = 1;
        iframe.width = 1;
        iframe.style.position = 'absolute';
        iframe.style.top = 0;
        iframe.style.left = 0;
        iframe.style.border = 'none';
        iframe.style.visibility = 'hidden';
        document.body.appendChild(iframe);

        if (document.readyState !== 'loading') {
            injectScript();
        } else if (window.addEventListener) {
            document.addEventListener('DOMContentLoaded', injectScript);
        } else {
            var originalOnReadyStateChange = document.onreadystatechange || function() {};
            document.onreadystatechange = function(event) {
                originalOnReadyStateChange(event);
                if (document.readyState !== 'loading') {
                    document.onreadystatechange = originalOnReadyStateChange;
                    injectScript();
                }
            };
        }
    }
})();
// ----------------------------- //