from abc import ABC, abstractmethod

# **🟦 Enterprise 고객**
# 저장소: AWS S3
#
# 썸네일 생성: AWS Lambda Image Processor
#
# 메타데이터: AWS MediaConvert
#
# URL 생성: CloudFront Signed URL
#
# **🟩 Startup 고객**
#
# 저장소: Local Storage
#
# 썸네일 생성: Pillow 기반 서버 처리
#
# 메타데이터: FFmpeg
#
# URL 생성: Static URL Builder
#
# **🟨 Privacy 고객 (보안 중요)**
#
# 저장소: Private Object Storage
#
# 썸네일 생성: 내부 폐쇄망 처리 서버
#
# 메타데이터: 내부 분석 서비스
#
# URL 생성: Token 기반 임시 URL


class Factory(ABC):
    @abstractmethod
    def create_Storage(self):
        pass

    def create_Thumbnail(self):
        pass

    def create_Metadata(self):
        pass

    def create_Url(self):
        pass


class Enterprise_factory(Factory):
    @abstractmethod
    def create_Storage(self):
        pass

    def create_Thumbnail(self):
        pass

    def create_Metadata(self):
        pass

    def create_Url(self):
        pass


class Startup_factory(Factory):
    @abstractmethod
    def create_Storage(self):
        pass

    def create_Thumbnail(self):
        pass

    def create_Metadata(self):
        pass

    def create_Url(self):
        pass


class Privacy_factory(Factory):
    @abstractmethod
    def create_Storage(self):
        pass

    def create_Thumbnail(self):
        pass

    def create_Metadata(self):
        pass

    def create_Url(self):
        pass