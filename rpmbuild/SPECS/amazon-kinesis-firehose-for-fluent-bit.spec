Summary: A Fluent Bit output plugin for Amazon Kinesis Firehose
Name: amazon-kinesis-firehose-for-fluent-bit
Version: 1.2.0
Release: 1%{?dist}
URL: https://github.com/aws/amazon-kinesis-firehose-for-fluent-bit
License: Apache v2.0
Group: Applications/File
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, git, make

%description
A Fluent Bit output plugin for Amazon Kinesis Firehose

%prep

%build
rm -fr %{buildroot}
git clone https://github.com/aws/amazon-kinesis-firehose-for-fluent-bit.git
git -C amazon-kinesis-firehose-for-fluent-bit checkout -f "v1.2.0"
make -C amazon-kinesis-firehose-for-fluent-bit release

%install

mkdir -p %{buildroot}/usr/local/lib/fluent-bit
install -m 644 -p amazon-kinesis-firehose-for-fluent-bit/bin/firehose.so \
    %{buildroot}/usr/local/lib/fluent-bit/firehose.so

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root,-)
/usr/local/lib/fluent-bit/firehose.so

%changelog
* Thu Mar 12 2020 Ichinose Shogo <shogo82148@gmail.com> - 1.1.0-1
- bump up to v1.2.0

* Fri Dec 13 2019 Ichinose Shogo <shogo82148@gmail.com> - 1.1.0-1
- bump up to v1.1.0
- update Go to 1.13.5

* Thu Nov 28 2019 Ichinose Shogo <shogo82148@gmail.com> - 1.0.0-1
- bump up to v1.0.0
- update Go to 1.13.4

* Sat Oct 12 2019 Ichinose Shogo <shogo82148@gmail.com> - 0.0.0-1
- first release
