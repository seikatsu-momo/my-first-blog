


self.addEventListener('install', event => {
    event.waitUntil(
        caches.open('v1').then(cache => {
            return cache.addAll([
                '/',
            ]);
        })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});


//オフラインキャッシュ
const CACHE = 'v1';

self.addEventListener('install', e => {
    e.waitUntil(
        caches.open(CACHE).then(c =>
            c.addAll([
                '/',
                '/static/js/main.js',
                '/static/css/style.css'
            ])
        )
    );
});

self.addEventListener('fetch', e => {
    e.respondWith(
        caches.match(e.request).then(r => r || fetch(e.request))
    );
});
