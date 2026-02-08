from locust import HttpUser, task, between

class RedditPerformanceUser(HttpUser):
    # İstifadəçilər hər hərəkət arası 1-3 saniyə gözləyir
    wait_time = between(1, 3)

    @task(2)
    def load_main_page(self):
        """Ana səhifənin yüklənmə sürətini yoxlayır"""
        self.client.get("/", name="Home Page")

    @task(1)
    def search_stress_test(self):
        """Axtarış API-sini yük altında yoxlayır"""
        self.client.get("/search/?q=automation", name="Search Performance")
