const CACHE_NAME = "kensaku-v1";

const urlsToCache = [
    "/",
    "/static/kensaku/css/style.css",
    "/static/js/sw-register.js",
    "/static/kensaku/css/bootstrap.min.css",
    "/static/icons/icon-192.png",
    "/static/icons/icon-512.png"
];

self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.addAll(urlsToCache);
        })
    );
});

self.addEventListener("fetch", event => {

    if (event.request.method !== "GET") return;

    event.respondWith(
        caches.match(event.request).then(response => {

            if (response) {
                return response;
            }

            return fetch(event.request).then(networkResponse => {

                if (!networkResponse || networkResponse.status !== 200) {
                    return networkResponse;
                }

                const cloned = networkResponse.clone();

                caches.open(CACHE_NAME).then(cache => {
                    cache.put(event.request, cloned);
                });

                return networkResponse;

            }).catch(() => {
                return caches.match("/");
            });

        })
    );
});

self.addEventListener("activate", event => {

    const whitelist = ["kensaku-v1"];

    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(
                keys.map(key => {
                    if (!whitelist.includes(key)) {
                        return caches.delete(key);
                    }
                })
            );
        })
    );
});