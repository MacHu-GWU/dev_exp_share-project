# -*- coding: utf-8 -*-

"""
This is an importable library can securely transfer file / folder across
monitored network. It uses AWS S3 to store the encrypted data and use symmetric
encryption algorithm to encrypt / decrypt the data.

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
from windtalker.api import SymmetricCipher


@dataclasses.dataclass
class App:
    """
    Secure file transfer app.
    """

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

        :param bsm: the boto3 session manager you want to use
        :param bucket: which s3 bucket to store the encrypted data
        :param folder: which folder in the s3 bucket to store the encrypted data
        :param password: the password you want to use to encrypt the data
        :param dir_tmp: the temp dir you want to use to store the temporary data,
            by default, it is ``${HOME}/tmp``.
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
        """

        :param archive_name: a unique name for the archive.
        :param path: which file / dir you want to transfer.
        :param overwrite: if True, overwrite existing file in AWS S3.
        """
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
            dir_tmp_archive = self._dir_tmp.joinpath(archive_name)
            try:
                dir_tmp_archive.mkdir_if_not_exists()

                path_output = dir_tmp_archive.joinpath(path.basename)
                self._cipher.encrypt_dir(
                    path=path,
                    output_path=path_output,
                    overwrite=overwrite,
                )
                path_output_zip = dir_tmp_archive.joinpath(path.basename + ".zip")
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
            except Exception as e:
                shutil.rmtree(dir_tmp_archive.abspath)
                raise e
            return s3path
        else:  # pragma: no cover
            raise NotImplementedError

    def download(
        self,
        archive_name: str,
        path: T.Optional[T_PATH_ARG] = None,
        overwrite: bool = True,
    ):
        """

        :param archive_name: a unique name for the archive.
        :param path: where you want to store the downloaded file / dir.
            if None, download to current working directory.
        :param overwrite: if True, overwrite existing file / dir.
        """
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
            dir_tmp_archive = self._dir_tmp.joinpath(archive_name)
            try:
                dir_tmp_archive.mkdir_if_not_exists()
                path_tmp_zip = dir_tmp_archive.joinpath(
                    s3path.metadata["dirname"] + ".zip"
                )
                self.bsm.s3_client.download_file(
                    Bucket=s3path.bucket,
                    Key=s3path.key,
                    Filename=path_tmp_zip.abspath,
                )
                shutil.unpack_archive(path_tmp_zip.abspath, dir_tmp_archive.abspath)
                dir_extracted = dir_tmp_archive.joinpath(s3path.metadata["dirname"])

                if path is None:
                    dir_here = Path.cwd()
                    self._cipher.decrypt_dir(
                        path=dir_extracted,
                        output_path=dir_here.joinpath(s3path.metadata["dirname"]),
                        overwrite=overwrite,
                    )
                else:
                    self._cipher.decrypt_dir(
                        path=dir_extracted,
                        output_path=path,
                        overwrite=overwrite,
                    )

            except Exception as e:
                shutil.rmtree(dir_tmp_archive.abspath)
                raise e
