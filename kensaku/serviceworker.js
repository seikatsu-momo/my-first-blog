



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
const CACHE_NAME = "kensaku-v1";

self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.add("/");
        })
    );
});

self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request).then(response => {

            // キャッシュにあればそれを返す
            if (response) {
                return response;
            }

            // なければネットから取得
            return fetch(event.request).then(networkResponse => {

                // キャッシュに保存
                return caches.open(CACHE_NAME).then(cache => {
                    cache.put(event.request, networkResponse.clone());
                    return networkResponse;
                });

            }).catch(() => {
                // 完全オフライン時
                return caches.match("/");
            });

        })
    );
});
