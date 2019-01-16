# fedora-deepin-common.ks
#
# Description:
# – Kickstart file for Fedora live media with the Deepin desktop environment
#
# Maintainer(s):
# – Zamir SUN <zsun@fedoraproject.org>
#

%packages
@networkmanager-submodules
sddm
deepin-desktop

# deepin applications
deepin-calendar
deepin-calculator
deepin-editor
deepin-image-viewer
# deepin-picker is not needed
deepin-screenshot
deepin-system-monitor

firefox
# l10n

# MP3
gstreamer1-plugin-mpg123

# Text Editor

# remove unneeded stuff to get a lightweight system
# fonts (we make no bones about admitting we're english-only)
# wqy-microhei-fonts          # a compact CJK font, to replace:
# -naver-nanum-gothic-fonts       # Korean
# -vlgothic-fonts             # Japanese
# -adobe-source-han-sans-cn-fonts     # simplified Chinese
# -adobe-source-han-sans-tw-fonts     # traditional Chinese

# -paratype-pt-sans-fonts # Cyrillic (already supported by DejaVu), huge
#-stix-fonts        # mathematical symbols

# remove input methods to free space
-@input-methods
-scim*
-m17n*
# Temporary include ibus to workaround RHBZ 1633225
# -ibus*
-iok

# Fix https://bugzilla.redhat.com/show_bug.cgi?id=1429132
# Why is this not pulled in by anaconda???
storaged

@admin-tools

%end

