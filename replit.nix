{ pkgs }: {
  deps = [
    pkgs.gettext
    pkgs.glibcLocales
    pkgs.po4a
    pkgs.gcc
    pkgs.autoconf
  ];
  env = {
    LC_ALL = "en_US.UTF-8";
    LANG = "en_US.UTF-8";
    LOCALE_ARCHIVE = "${pkgs.glibcLocales}/lib/locale/locale-archive";
  }
}