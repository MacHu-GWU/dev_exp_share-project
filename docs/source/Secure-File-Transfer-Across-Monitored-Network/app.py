# -*- coding: utf-8 -*-

"""
This is an importable Python library that can

make a zip archive for a folder, encrypt it and upload to AWS S3.
then download it from AWS S3 on another machine and decrypt it.

Requirements:

- Python >= 3.7
- Dependencies::

    boto3
    boto_session_manager>=1.7.2,<2.0.0
    s3pathlib>=2.1.2,<3.0.0
    windtalker>=1.0.1,<2.0.0
"""

import typing as T
import shutil
import dataclasses

from pathlib_mate import Path, T_PATH_ARG
from boto_session_manager import BotoSesManager
from s3pathlib import S3Path
from pathlib_mate import Path
from windtalker.api import SymmetricCipher


@dataclasses.dataclass
class App:
    bsm: BotoSesManager = dataclasses.field()
    bucket: str = dataclasses.field()
    folder: str = dataclasses.field()
    _dir_tmp: Path = dataclasses.field()
    _cipher: SymmetricCipher = dataclasses.field()
    _s3dir: S3Path = dataclasses.field()

    @classmethod
    def new(
        cls,
        bsm: BotoSesManager,
        bucket: str,
        folder: str,
        password: T.Optional[str] = None,
        dir_tmp: T.Optional[T_PATH_ARG] = None,
    ):
        """
        Create a new instance of App.
        """
        if dir_tmp is None:
            dir_tmp = Path.home().joinpath("tmp")
            dir_tmp.mkdir_if_not_exists()
        else:
            dir_tmp = Path(dir_tmp)
        return cls(
            bsm=bsm,
            bucket=bucket,
            folder=folder,
            _cipher=SymmetricCipher(password=password),
            _s3dir=S3Path(bucket, folder).to_dir(),
            _dir_tmp=dir_tmp,
        )

    def upload(
        self,
        archive_name: str,
        path: T_PATH_ARG,
        overwrite: bool = True,
    ) -> S3Path:
        path = Path(path).absolute()
        s3path = self._s3dir.joinpath(archive_name, "encrypted")

        # --- file logic
        if path.is_file():
            if overwrite is False:  # pragma: no cover
                if s3path.exists(bsm=self.bsm) is True:
                    raise FileExistsError(f"{s3path.uri} already exists.")

            s3path.write_bytes(
                data=self._cipher.encrypt_binary(path.read_bytes()),
                metadata={
                    "type": "file",
                    "filename": path.basename,
                },
                bsm=self.bsm,
            )
            return s3path

        # --- dir logic
        elif path.is_dir():
            path_output = self._dir_tmp.joinpath(archive_name)
            self._cipher.encrypt_dir(
                path=path,
                output_path=path_output,
                overwrite=overwrite,
            )
            path_output_zip = self._dir_tmp.joinpath(archive_name + ".zip")
            path_output.make_zip_archive(
                dst=path_output_zip,
                overwrite=overwrite,
                include_dir=True,
            )
            s3path.upload_file(
                path_output_zip,
                extra_args=dict(
                    Metadata={
                        "type": "dir",
                        "dirname": path.basename,
                    }
                ),
                overwrite=overwrite,
            )
        else:  # pragma: no cover
            raise NotImplementedError

    def download(
        self,
        archive_name: str,
        path: T.Optional[T_PATH_ARG] = None,
        overwrite: bool = True,
    ):
        s3path = self._s3dir.joinpath(archive_name, "encrypted")

        # --- file logic
        if s3path.metadata["type"] == "file":
            if path is None:
                path = Path.cwd().joinpath(s3path.metadata["filename"])
            else:
                path = Path(path).absolute()
            if path.exists() and overwrite is False:
                raise FileExistsError(f"{path} already exists.")
            path.write_bytes(self._cipher.decrypt_binary(s3path.read_bytes()))

        # --- dir logic
        elif s3path.metadata["type"] == "dir":
            if path is None:
                dir_here = Path.cwd()
                path_tmp_zip = self._dir_tmp.joinpath(s3path.metadata["dirname"] + ".zip")
                self.bsm.s3_client.download_file(
                    Bucket=s3path.bucket,
                    Key=s3path.key,
                    Filename=path_tmp_zip.abspath,
                )
                dir_extracted = self._dir_tmp.joinpath(s3path.metadata["dirname"])
                shutil.unpack_archive(path_tmp_zip.abspath, dir_extracted.abspath)
                self._cipher.decrypt_dir(
                    path=path_tmp_zip,
                    output_path=path,
                    overwrite=overwrite,
                )


#
# class Config:
#     PASSWORD = "password_here"  # the password you use to encrypt the file
#     AWS_PROFILE = "aws_profile_here"  # aws profile
#     BUCKET = "s3_bucket_name"
#     KEY = "s3_key"
#
#
# p_source = Path(__file__).change(new_basename="test-data") # the folder you want to upload
# p_archive = p_source.change(new_basename="data-sender.zip") # the temp archive file
# p_encrypted_archive = p_archive.change(new_basename="data-sender.dat") # the temp encrypted data file
# p_encrypted_archive_downloads = p_source.change(new_basename="data-receiver.dat") # the temp encrypted data file
# p_archive_downloads = p_encrypted_archive_downloads.change(new_basename="data-receiver.zip") # the temp decrypted data archive
#
# c = SymmetricCipher(password=Config.PASSWORD)
# boto_ses = boto3.session.Session(profile_name=Config.AWS_PROFILE)
# s3_client = boto_ses.client("s3")
#
#
# def upload():
#     p_source.make_zip_archive(dst=p_archive, overwrite=True)
#     c.encrypt_file(p_archive.abspath, output_path=p_encrypted_archive.abspath, overwrite=True)
#     with open(p_encrypted_archive.abspath, "rb") as f:
#         s3_client.put_object(Bucket=Config.BUCKET, Key=Config.KEY, Body=f.read())
#
#
# def download():
#     response = s3_client.get_object(Bucket=Config.BUCKET, Key=Config.KEY)
#     with open(p_encrypted_archive_downloads.abspath, "wb") as f:
#         f.write(response["Body"].read())
#     c.decrypt_file(p_encrypted_archive_downloads.abspath, p_archive_downloads.abspath)


if __name__ == "__main__":
    # upload()
    # download()
    pass
