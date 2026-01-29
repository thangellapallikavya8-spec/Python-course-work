# Feature class (no inheritance)
class Feature:
    def __init__(self, feature_name):
        self.feature_name = feature_name

    def use_feature(self):
        return f"{self.feature_name} feature used"


# Developer class (Encapsulation)
class Developer:
    def __init__(self, name, contact, location):
        self.__name = name
        self.__contact = contact
        self.__location = location

    def show_developer(self):
        print(f"Developer Name: {self.__name}")
        print(f"Contact: {self.__contact}")
        print(f"Location: {self.__location}")


# TikTok App class
class TikTokApp:
    total_apps = 0

    def __init__(self, app_id, version):
        self.app_id = app_id
        self.name = "TikTok"
        self.version = version
        self.price = 0.0
        self.categories = []
        self.features = []
        self.developer = None
        TikTokApp.total_apps += 1

    def add_category(self, category):
        self.categories.append(category)

    def add_feature(self, feature):
        self.features.append(feature)

    def set_developer(self, developer):
        self.developer = developer

    def display_info(self):
        print("\nApp ID:", self.app_id)
        print("Name:", self.name)
        print("Version:", self.version)
        print("Price:", self.price)
        print("Categories:", ", ".join(self.categories))
        print("Features:")
        for f in self.features:
            print("-", f.use_feature())
        print("\nDeveloper Details:")
        self.developer.show_developer()

    @classmethod
    def total_apps_created(cls):
        return cls.total_apps


# Create developer
dev = Developer("ByteDance Ltd.", "support@tiktok.com", "Beijing, China")

# Create TikTok app
tiktok = TikTokApp(201, "34.2.1")

# Add categories
tiktok.add_category("Social Media")
tiktok.add_category("Entertainment")
tiktok.add_category("Video Sharing")

# Add features
tiktok.add_feature(Feature("Video Upload"))
tiktok.add_feature(Feature("Live Streaming"))
tiktok.add_feature(Feature("Filters & Effects"))
tiktok.add_feature(Feature("Duet"))

# Assign developer
tiktok.set_developer(dev)

# Display details
tiktok.display_info()
print("\nTotal Apps Created:", TikTokApp.total_apps_created())
