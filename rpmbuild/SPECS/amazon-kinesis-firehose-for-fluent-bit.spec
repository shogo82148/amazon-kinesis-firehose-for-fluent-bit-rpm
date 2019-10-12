Summary: A Fluent Bit output plugin for Amazon Kinesis Firehose
Name: amazon-kinesis-firehose-for-fluent-bit
Version: 0.0.0
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
git clone --depth 10 https://github.com/aws/amazon-kinesis-firehose-for-fluent-bit.git
git -C amazon-kinesis-firehose-for-fluent-bit checkout 0883cb76f5116b192adf0485b095050675486165
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
* Sat Oct 12 2019 Ichinose Shogo <shogo82148@gmail.com> - 0.0.0-1
- first release
