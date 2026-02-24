from abc import ABC, abstractmethod

################################### 인터페이스 ###################################
class Storage (ABC):
    @abstractmethod
    def save (self):
        pass

class Thumbnail(ABC):
    @abstractmethod
    def create_thumbnail (self):
        pass


class Metadata(ABC):
    @abstractmethod
    def create_metadata (self):
        pass


class URL(ABC):
    @abstractmethod
    def create_url (self):
        pass

# 추상 팩토리
class AbstractFactory(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def create_thumbnail(self):
        pass

    @abstractmethod
    def create_metadata(self):
        pass

    @abstractmethod
    def create_url (self):
        pass



################################### 구체 제품 ###################################


# 🟦 Enterprise 고객
# 저장소: AWS S3
#
# 썸네일 생성: AWS Lambda Image Processor
#
# 메타데이터: AWS MediaConvert
#
# URL 생성: CloudFront Signed URL

class EnterpriseStorage(Storage):
    def save (self):
        print("저장소: AWS S3")


class EnterpriseThumbnail(Thumbnail):
    def create_thumbnail (self):
        print("썸네일 생성: AWS Lambda Image Processor")


class EnterpriseMetadata(Metadata):
    def create_metadata (self):
        print("메타데이터: AWS MediaConvert")


class EnterpriseURL(URL):
    def create_url (self):
        print("URL 생성: CloudFront Signed URL")

# **🟩 Startup 고객**
#
# 저장소: Local Storage
#
# 썸네일 생성: Pillow 기반 서버 처리
#
# 메타데이터: FFmpeg
#
# URL 생성: Static URL Builder

class StartupStorage(Storage):
    def save (self):
        print("저장소: Local Storage")


class StartupThumbnail(Thumbnail):
    def create_thumbnail(self):
        print("썸네일 생성: Pillow 기반 서버 처리")


class StartupMetadata(Metadata):
    def create_metadata(self):
        print("메타데이터: FFmpeg")


class StartupURL(URL):
    def create_url(self):
        print("URL 생성: Static URL Builder")


# **🟨 Privacy 고객 (보안 중요)**
#
# 저장소: Private Object Storage
#
# 썸네일 생성: 내부 폐쇄망 처리 서버
#
# 메타데이터: 내부 분석 서비스
#
# URL 생성: Token 기반 임시 URL


class PrivacyStorage(Storage):
    def save(self):
        print("저장소: Private Object Storage")


class PrivacyThumbnail(Thumbnail):
    def create_thumbnail(self):
        print("썸네일 생성: 내부 폐쇄망 처리 서버")


class PrivacyMetadata(Metadata):
    def create_metadata(self):
        print("메타데이터: 내부 분석 서비스")


class PrivacyURL(URL):
    def create_url (self):
        print("URL 생성: Token 기반 임시 URL")

# ⬛ Streaming Pro 고객
#
# 저장소: Streaming Pro Storage
#
# 썸네일 생성: Streaming Pro 서버
#
# 메타데이터: Streaming Pro 서비스
#
# URL 생성: Streaming Pro URL

class StreamingProStorage(Storage):
    def save(self):
        print("저장소: Streaming Pro Storage")


class StreamingProThumbnail(Thumbnail):
    def create_thumbnail(self):
        print("Streaming Pro 서버")


class StreamingProMetadata(Metadata):
    def create_metadata(self):
        print("Streaming Pro 서비스")


class StreamingProURL(URL):
    def create_url (self):
        print("Streaming Pro URL")


######################################### 구체 팩토리 ###################################
# 🟦 Enterprise 고객
class EnterpriseFactory(AbstractFactory):
    def save (self):
        return EnterpriseStorage()
    def create_thumbnail (self):
        return EnterpriseThumbnail()
    def create_metadata (self):
        return EnterpriseMetadata()
    def create_url (self):
        return EnterpriseURL()


# **🟩 Startup 고객**
class StartupFactory(AbstractFactory):
    def save (self):
        return StartupStorage()
    def create_thumbnail (self):
        return StartupThumbnail()
    def create_metadata (self):
        return StartupMetadata()
    def create_url (self):
        return StartupURL()


# **🟨 Privacy 고객 (보안 중요)**
class PrivacyFactory(AbstractFactory):
    def save (self):
        return PrivacyStorage()
    def create_thumbnail (self):
        return PrivacyThumbnail()
    def create_metadata (self):
        return PrivacyMetadata()
    def create_url (self):
        return PrivacyURL()

# **⬛ StreamingPro 고객
class StreamingProFactory(AbstractFactory):
    def save (self):
        return StreamingProStorage()
    def create_thumbnail (self):
        return StreamingProThumbnail()
    def create_metadata (self):
        return StreamingProMetadata()
    def create_url (self):
        return StreamingProURL()



# 클라이언트

class Upload():

    def __init__(self, factory: AbstractFactory):
        self.storage = factory.save()
        self.thumbnail = factory.create_thumbnail()
        self.metadata = factory.create_metadata()
        self.url_builder = factory.create_url()

    def upload(self, data):
        self.storage.save()
        self.thumbnail.create_thumbnail()
        self.metadata.create_metadata()
        self.url_builder.create_url()
        print(f"업로드 파일 :{data}")


if __name__ == "__main__":

    # 구체 클래스를 몰라도 된다.
    # 공장만 바꾸면 통째로 바뀐다.

    Upload(EnterpriseFactory()).upload("1번 파일")
    print("============================")

    Upload(StartupFactory()).upload("2번 파일")

    print("============================")

    Upload(PrivacyFactory()).upload("3번 파일")

    print("============================")

    Upload(StreamingProFactory()).upload("4번 파일")

