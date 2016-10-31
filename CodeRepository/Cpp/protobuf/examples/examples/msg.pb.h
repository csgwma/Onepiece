// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: examples/msg.proto

#ifndef PROTOBUF_examples_2fmsg_2eproto__INCLUDED
#define PROTOBUF_examples_2fmsg_2eproto__INCLUDED

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 3000000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 3000002 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/generated_enum_reflection.h>
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)

// Internal implementation detail -- do not call these.
void protobuf_AddDesc_examples_2fmsg_2eproto();
void protobuf_AssignDesc_examples_2fmsg_2eproto();
void protobuf_ShutdownFile_examples_2fmsg_2eproto();

class AddressBook;
class Person;
class Person_CountryInfo;
class Person_PhoneNumber;

enum Person_PhoneType {
  Person_PhoneType_MOBILE = 0,
  Person_PhoneType_HOME = 1,
  Person_PhoneType_WORK = 2
};
bool Person_PhoneType_IsValid(int value);
const Person_PhoneType Person_PhoneType_PhoneType_MIN = Person_PhoneType_MOBILE;
const Person_PhoneType Person_PhoneType_PhoneType_MAX = Person_PhoneType_WORK;
const int Person_PhoneType_PhoneType_ARRAYSIZE = Person_PhoneType_PhoneType_MAX + 1;

const ::google::protobuf::EnumDescriptor* Person_PhoneType_descriptor();
inline const ::std::string& Person_PhoneType_Name(Person_PhoneType value) {
  return ::google::protobuf::internal::NameOfEnum(
    Person_PhoneType_descriptor(), value);
}
inline bool Person_PhoneType_Parse(
    const ::std::string& name, Person_PhoneType* value) {
  return ::google::protobuf::internal::ParseNamedEnum<Person_PhoneType>(
    Person_PhoneType_descriptor(), name, value);
}
// ===================================================================

class Person_PhoneNumber : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:Person.PhoneNumber) */ {
 public:
  Person_PhoneNumber();
  virtual ~Person_PhoneNumber();

  Person_PhoneNumber(const Person_PhoneNumber& from);

  inline Person_PhoneNumber& operator=(const Person_PhoneNumber& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _internal_metadata_.unknown_fields();
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return _internal_metadata_.mutable_unknown_fields();
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const Person_PhoneNumber& default_instance();

  void Swap(Person_PhoneNumber* other);

  // implements Message ----------------------------------------------

  inline Person_PhoneNumber* New() const { return New(NULL); }

  Person_PhoneNumber* New(::google::protobuf::Arena* arena) const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const Person_PhoneNumber& from);
  void MergeFrom(const Person_PhoneNumber& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const {
    return InternalSerializeWithCachedSizesToArray(false, output);
  }
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  void InternalSwap(Person_PhoneNumber* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return _internal_metadata_.arena();
  }
  inline void* MaybeArenaPtr() const {
    return _internal_metadata_.raw_arena_ptr();
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // required string number = 1;
  bool has_number() const;
  void clear_number();
  static const int kNumberFieldNumber = 1;
  const ::std::string& number() const;
  void set_number(const ::std::string& value);
  void set_number(const char* value);
  void set_number(const char* value, size_t size);
  ::std::string* mutable_number();
  ::std::string* release_number();
  void set_allocated_number(::std::string* number);

  // optional .Person.PhoneType type = 2 [default = HOME];
  bool has_type() const;
  void clear_type();
  static const int kTypeFieldNumber = 2;
  ::Person_PhoneType type() const;
  void set_type(::Person_PhoneType value);

  // @@protoc_insertion_point(class_scope:Person.PhoneNumber)
 private:
  inline void set_has_number();
  inline void clear_has_number();
  inline void set_has_type();
  inline void clear_has_type();

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::uint32 _has_bits_[1];
  mutable int _cached_size_;
  ::google::protobuf::internal::ArenaStringPtr number_;
  int type_;
  friend void  protobuf_AddDesc_examples_2fmsg_2eproto();
  friend void protobuf_AssignDesc_examples_2fmsg_2eproto();
  friend void protobuf_ShutdownFile_examples_2fmsg_2eproto();

  void InitAsDefaultInstance();
  static Person_PhoneNumber* default_instance_;
};
// -------------------------------------------------------------------

class Person_CountryInfo : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:Person.CountryInfo) */ {
 public:
  Person_CountryInfo();
  virtual ~Person_CountryInfo();

  Person_CountryInfo(const Person_CountryInfo& from);

  inline Person_CountryInfo& operator=(const Person_CountryInfo& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _internal_metadata_.unknown_fields();
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return _internal_metadata_.mutable_unknown_fields();
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const Person_CountryInfo& default_instance();

  void Swap(Person_CountryInfo* other);

  // implements Message ----------------------------------------------

  inline Person_CountryInfo* New() const { return New(NULL); }

  Person_CountryInfo* New(::google::protobuf::Arena* arena) const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const Person_CountryInfo& from);
  void MergeFrom(const Person_CountryInfo& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const {
    return InternalSerializeWithCachedSizesToArray(false, output);
  }
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  void InternalSwap(Person_CountryInfo* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return _internal_metadata_.arena();
  }
  inline void* MaybeArenaPtr() const {
    return _internal_metadata_.raw_arena_ptr();
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // required string name = 1;
  bool has_name() const;
  void clear_name();
  static const int kNameFieldNumber = 1;
  const ::std::string& name() const;
  void set_name(const ::std::string& value);
  void set_name(const char* value);
  void set_name(const char* value, size_t size);
  ::std::string* mutable_name();
  ::std::string* release_name();
  void set_allocated_name(::std::string* name);

  // required string code = 2;
  bool has_code() const;
  void clear_code();
  static const int kCodeFieldNumber = 2;
  const ::std::string& code() const;
  void set_code(const ::std::string& value);
  void set_code(const char* value);
  void set_code(const char* value, size_t size);
  ::std::string* mutable_code();
  ::std::string* release_code();
  void set_allocated_code(::std::string* code);

  // optional int32 number = 3;
  bool has_number() const;
  void clear_number();
  static const int kNumberFieldNumber = 3;
  ::google::protobuf::int32 number() const;
  void set_number(::google::protobuf::int32 value);

  // @@protoc_insertion_point(class_scope:Person.CountryInfo)
 private:
  inline void set_has_name();
  inline void clear_has_name();
  inline void set_has_code();
  inline void clear_has_code();
  inline void set_has_number();
  inline void clear_has_number();

  // helper for ByteSize()
  int RequiredFieldsByteSizeFallback() const;

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::uint32 _has_bits_[1];
  mutable int _cached_size_;
  ::google::protobuf::internal::ArenaStringPtr name_;
  ::google::protobuf::internal::ArenaStringPtr code_;
  ::google::protobuf::int32 number_;
  friend void  protobuf_AddDesc_examples_2fmsg_2eproto();
  friend void protobuf_AssignDesc_examples_2fmsg_2eproto();
  friend void protobuf_ShutdownFile_examples_2fmsg_2eproto();

  void InitAsDefaultInstance();
  static Person_CountryInfo* default_instance_;
};
// -------------------------------------------------------------------

class Person : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:Person) */ {
 public:
  Person();
  virtual ~Person();

  Person(const Person& from);

  inline Person& operator=(const Person& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _internal_metadata_.unknown_fields();
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return _internal_metadata_.mutable_unknown_fields();
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const Person& default_instance();

  void Swap(Person* other);

  // implements Message ----------------------------------------------

  inline Person* New() const { return New(NULL); }

  Person* New(::google::protobuf::Arena* arena) const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const Person& from);
  void MergeFrom(const Person& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const {
    return InternalSerializeWithCachedSizesToArray(false, output);
  }
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  void InternalSwap(Person* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return _internal_metadata_.arena();
  }
  inline void* MaybeArenaPtr() const {
    return _internal_metadata_.raw_arena_ptr();
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  typedef Person_PhoneNumber PhoneNumber;
  typedef Person_CountryInfo CountryInfo;

  typedef Person_PhoneType PhoneType;
  static const PhoneType MOBILE =
    Person_PhoneType_MOBILE;
  static const PhoneType HOME =
    Person_PhoneType_HOME;
  static const PhoneType WORK =
    Person_PhoneType_WORK;
  static inline bool PhoneType_IsValid(int value) {
    return Person_PhoneType_IsValid(value);
  }
  static const PhoneType PhoneType_MIN =
    Person_PhoneType_PhoneType_MIN;
  static const PhoneType PhoneType_MAX =
    Person_PhoneType_PhoneType_MAX;
  static const int PhoneType_ARRAYSIZE =
    Person_PhoneType_PhoneType_ARRAYSIZE;
  static inline const ::google::protobuf::EnumDescriptor*
  PhoneType_descriptor() {
    return Person_PhoneType_descriptor();
  }
  static inline const ::std::string& PhoneType_Name(PhoneType value) {
    return Person_PhoneType_Name(value);
  }
  static inline bool PhoneType_Parse(const ::std::string& name,
      PhoneType* value) {
    return Person_PhoneType_Parse(name, value);
  }

  // accessors -------------------------------------------------------

  // required string name = 1;
  bool has_name() const;
  void clear_name();
  static const int kNameFieldNumber = 1;
  const ::std::string& name() const;
  void set_name(const ::std::string& value);
  void set_name(const char* value);
  void set_name(const char* value, size_t size);
  ::std::string* mutable_name();
  ::std::string* release_name();
  void set_allocated_name(::std::string* name);

  // required int32 id = 2;
  bool has_id() const;
  void clear_id();
  static const int kIdFieldNumber = 2;
  ::google::protobuf::int32 id() const;
  void set_id(::google::protobuf::int32 value);

  // optional string email = 3;
  bool has_email() const;
  void clear_email();
  static const int kEmailFieldNumber = 3;
  const ::std::string& email() const;
  void set_email(const ::std::string& value);
  void set_email(const char* value);
  void set_email(const char* value, size_t size);
  ::std::string* mutable_email();
  ::std::string* release_email();
  void set_allocated_email(::std::string* email);

  // repeated .Person.PhoneNumber phone = 4;
  int phone_size() const;
  void clear_phone();
  static const int kPhoneFieldNumber = 4;
  const ::Person_PhoneNumber& phone(int index) const;
  ::Person_PhoneNumber* mutable_phone(int index);
  ::Person_PhoneNumber* add_phone();
  ::google::protobuf::RepeatedPtrField< ::Person_PhoneNumber >*
      mutable_phone();
  const ::google::protobuf::RepeatedPtrField< ::Person_PhoneNumber >&
      phone() const;

  // @@protoc_insertion_point(class_scope:Person)
 private:
  inline void set_has_name();
  inline void clear_has_name();
  inline void set_has_id();
  inline void clear_has_id();
  inline void set_has_email();
  inline void clear_has_email();

  // helper for ByteSize()
  int RequiredFieldsByteSizeFallback() const;

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::uint32 _has_bits_[1];
  mutable int _cached_size_;
  ::google::protobuf::internal::ArenaStringPtr name_;
  ::google::protobuf::internal::ArenaStringPtr email_;
  ::google::protobuf::RepeatedPtrField< ::Person_PhoneNumber > phone_;
  ::google::protobuf::int32 id_;
  friend void  protobuf_AddDesc_examples_2fmsg_2eproto();
  friend void protobuf_AssignDesc_examples_2fmsg_2eproto();
  friend void protobuf_ShutdownFile_examples_2fmsg_2eproto();

  void InitAsDefaultInstance();
  static Person* default_instance_;
};
// -------------------------------------------------------------------

class AddressBook : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:AddressBook) */ {
 public:
  AddressBook();
  virtual ~AddressBook();

  AddressBook(const AddressBook& from);

  inline AddressBook& operator=(const AddressBook& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _internal_metadata_.unknown_fields();
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return _internal_metadata_.mutable_unknown_fields();
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const AddressBook& default_instance();

  void Swap(AddressBook* other);

  // implements Message ----------------------------------------------

  inline AddressBook* New() const { return New(NULL); }

  AddressBook* New(::google::protobuf::Arena* arena) const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const AddressBook& from);
  void MergeFrom(const AddressBook& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const {
    return InternalSerializeWithCachedSizesToArray(false, output);
  }
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  void InternalSwap(AddressBook* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return _internal_metadata_.arena();
  }
  inline void* MaybeArenaPtr() const {
    return _internal_metadata_.raw_arena_ptr();
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // repeated .Person person = 1;
  int person_size() const;
  void clear_person();
  static const int kPersonFieldNumber = 1;
  const ::Person& person(int index) const;
  ::Person* mutable_person(int index);
  ::Person* add_person();
  ::google::protobuf::RepeatedPtrField< ::Person >*
      mutable_person();
  const ::google::protobuf::RepeatedPtrField< ::Person >&
      person() const;

  // @@protoc_insertion_point(class_scope:AddressBook)
 private:

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::uint32 _has_bits_[1];
  mutable int _cached_size_;
  ::google::protobuf::RepeatedPtrField< ::Person > person_;
  friend void  protobuf_AddDesc_examples_2fmsg_2eproto();
  friend void protobuf_AssignDesc_examples_2fmsg_2eproto();
  friend void protobuf_ShutdownFile_examples_2fmsg_2eproto();

  void InitAsDefaultInstance();
  static AddressBook* default_instance_;
};
// ===================================================================


// ===================================================================

#if !PROTOBUF_INLINE_NOT_IN_HEADERS
// Person_PhoneNumber

// required string number = 1;
inline bool Person_PhoneNumber::has_number() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void Person_PhoneNumber::set_has_number() {
  _has_bits_[0] |= 0x00000001u;
}
inline void Person_PhoneNumber::clear_has_number() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void Person_PhoneNumber::clear_number() {
  number_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  clear_has_number();
}
inline const ::std::string& Person_PhoneNumber::number() const {
  // @@protoc_insertion_point(field_get:Person.PhoneNumber.number)
  return number_.GetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Person_PhoneNumber::set_number(const ::std::string& value) {
  set_has_number();
  number_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:Person.PhoneNumber.number)
}
inline void Person_PhoneNumber::set_number(const char* value) {
  set_has_number();
  number_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:Person.PhoneNumber.number)
}
inline void Person_PhoneNumber::set_number(const char* value, size_t size) {
  set_has_number();
  number_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:Person.PhoneNumber.number)
}
inline ::std::string* Person_PhoneNumber::mutable_number() {
  set_has_number();
  // @@protoc_insertion_point(field_mutable:Person.PhoneNumber.number)
  return number_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline ::std::string* Person_PhoneNumber::release_number() {
  // @@protoc_insertion_point(field_release:Person.PhoneNumber.number)
  clear_has_number();
  return number_.ReleaseNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Person_PhoneNumber::set_allocated_number(::std::string* number) {
  if (number != NULL) {
    set_has_number();
  } else {
    clear_has_number();
  }
  number_.SetAllocatedNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), number);
  // @@protoc_insertion_point(field_set_allocated:Person.PhoneNumber.number)
}

// optional .Person.PhoneType type = 2 [default = HOME];
inline bool Person_PhoneNumber::has_type() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void Person_PhoneNumber::set_has_type() {
  _has_bits_[0] |= 0x00000002u;
}
inline void Person_PhoneNumber::clear_has_type() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void Person_PhoneNumber::clear_type() {
  type_ = 1;
  clear_has_type();
}
inline ::Person_PhoneType Person_PhoneNumber::type() const {
  // @@protoc_insertion_point(field_get:Person.PhoneNumber.type)
  return static_cast< ::Person_PhoneType >(type_);
}
inline void Person_PhoneNumber::set_type(::Person_PhoneType value) {
  assert(::Person_PhoneType_IsValid(value));
  set_has_type();
  type_ = value;
  // @@protoc_insertion_point(field_set:Person.PhoneNumber.type)
}

// -------------------------------------------------------------------

// Person_CountryInfo

// required string name = 1;
inline bool Person_CountryInfo::has_name() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void Person_CountryInfo::set_has_name() {
  _has_bits_[0] |= 0x00000001u;
}
inline void Person_CountryInfo::clear_has_name() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void Person_CountryInfo::clear_name() {
  name_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  clear_has_name();
}
inline const ::std::string& Person_CountryInfo::name() const {
  // @@protoc_insertion_point(field_get:Person.CountryInfo.name)
  return name_.GetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Person_CountryInfo::set_name(const ::std::string& value) {
  set_has_name();
  name_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:Person.CountryInfo.name)
}
inline void Person_CountryInfo::set_name(const char* value) {
  set_has_name();
  name_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:Person.CountryInfo.name)
}
inline void Person_CountryInfo::set_name(const char* value, size_t size) {
  set_has_name();
  name_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:Person.CountryInfo.name)
}
inline ::std::string* Person_CountryInfo::mutable_name() {
  set_has_name();
  // @@protoc_insertion_point(field_mutable:Person.CountryInfo.name)
  return name_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline ::std::string* Person_CountryInfo::release_name() {
  // @@protoc_insertion_point(field_release:Person.CountryInfo.name)
  clear_has_name();
  return name_.ReleaseNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Person_CountryInfo::set_allocated_name(::std::string* name) {
  if (name != NULL) {
    set_has_name();
  } else {
    clear_has_name();
  }
  name_.SetAllocatedNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), name);
  // @@protoc_insertion_point(field_set_allocated:Person.CountryInfo.name)
}

// required string code = 2;
inline bool Person_CountryInfo::has_code() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void Person_CountryInfo::set_has_code() {
  _has_bits_[0] |= 0x00000002u;
}
inline void Person_CountryInfo::clear_has_code() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void Person_CountryInfo::clear_code() {
  code_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  clear_has_code();
}
inline const ::std::string& Person_CountryInfo::code() const {
  // @@protoc_insertion_point(field_get:Person.CountryInfo.code)
  return code_.GetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Person_CountryInfo::set_code(const ::std::string& value) {
  set_has_code();
  code_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:Person.CountryInfo.code)
}
inline void Person_CountryInfo::set_code(const char* value) {
  set_has_code();
  code_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:Person.CountryInfo.code)
}
inline void Person_CountryInfo::set_code(const char* value, size_t size) {
  set_has_code();
  code_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:Person.CountryInfo.code)
}
inline ::std::string* Person_CountryInfo::mutable_code() {
  set_has_code();
  // @@protoc_insertion_point(field_mutable:Person.CountryInfo.code)
  return code_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline ::std::string* Person_CountryInfo::release_code() {
  // @@protoc_insertion_point(field_release:Person.CountryInfo.code)
  clear_has_code();
  return code_.ReleaseNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Person_CountryInfo::set_allocated_code(::std::string* code) {
  if (code != NULL) {
    set_has_code();
  } else {
    clear_has_code();
  }
  code_.SetAllocatedNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), code);
  // @@protoc_insertion_point(field_set_allocated:Person.CountryInfo.code)
}

// optional int32 number = 3;
inline bool Person_CountryInfo::has_number() const {
  return (_has_bits_[0] & 0x00000004u) != 0;
}
inline void Person_CountryInfo::set_has_number() {
  _has_bits_[0] |= 0x00000004u;
}
inline void Person_CountryInfo::clear_has_number() {
  _has_bits_[0] &= ~0x00000004u;
}
inline void Person_CountryInfo::clear_number() {
  number_ = 0;
  clear_has_number();
}
inline ::google::protobuf::int32 Person_CountryInfo::number() const {
  // @@protoc_insertion_point(field_get:Person.CountryInfo.number)
  return number_;
}
inline void Person_CountryInfo::set_number(::google::protobuf::int32 value) {
  set_has_number();
  number_ = value;
  // @@protoc_insertion_point(field_set:Person.CountryInfo.number)
}

// -------------------------------------------------------------------

// Person

// required string name = 1;
inline bool Person::has_name() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void Person::set_has_name() {
  _has_bits_[0] |= 0x00000001u;
}
inline void Person::clear_has_name() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void Person::clear_name() {
  name_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  clear_has_name();
}
inline const ::std::string& Person::name() const {
  // @@protoc_insertion_point(field_get:Person.name)
  return name_.GetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Person::set_name(const ::std::string& value) {
  set_has_name();
  name_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:Person.name)
}
inline void Person::set_name(const char* value) {
  set_has_name();
  name_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:Person.name)
}
inline void Person::set_name(const char* value, size_t size) {
  set_has_name();
  name_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:Person.name)
}
inline ::std::string* Person::mutable_name() {
  set_has_name();
  // @@protoc_insertion_point(field_mutable:Person.name)
  return name_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline ::std::string* Person::release_name() {
  // @@protoc_insertion_point(field_release:Person.name)
  clear_has_name();
  return name_.ReleaseNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Person::set_allocated_name(::std::string* name) {
  if (name != NULL) {
    set_has_name();
  } else {
    clear_has_name();
  }
  name_.SetAllocatedNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), name);
  // @@protoc_insertion_point(field_set_allocated:Person.name)
}

// required int32 id = 2;
inline bool Person::has_id() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void Person::set_has_id() {
  _has_bits_[0] |= 0x00000002u;
}
inline void Person::clear_has_id() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void Person::clear_id() {
  id_ = 0;
  clear_has_id();
}
inline ::google::protobuf::int32 Person::id() const {
  // @@protoc_insertion_point(field_get:Person.id)
  return id_;
}
inline void Person::set_id(::google::protobuf::int32 value) {
  set_has_id();
  id_ = value;
  // @@protoc_insertion_point(field_set:Person.id)
}

// optional string email = 3;
inline bool Person::has_email() const {
  return (_has_bits_[0] & 0x00000004u) != 0;
}
inline void Person::set_has_email() {
  _has_bits_[0] |= 0x00000004u;
}
inline void Person::clear_has_email() {
  _has_bits_[0] &= ~0x00000004u;
}
inline void Person::clear_email() {
  email_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  clear_has_email();
}
inline const ::std::string& Person::email() const {
  // @@protoc_insertion_point(field_get:Person.email)
  return email_.GetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Person::set_email(const ::std::string& value) {
  set_has_email();
  email_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:Person.email)
}
inline void Person::set_email(const char* value) {
  set_has_email();
  email_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:Person.email)
}
inline void Person::set_email(const char* value, size_t size) {
  set_has_email();
  email_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:Person.email)
}
inline ::std::string* Person::mutable_email() {
  set_has_email();
  // @@protoc_insertion_point(field_mutable:Person.email)
  return email_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline ::std::string* Person::release_email() {
  // @@protoc_insertion_point(field_release:Person.email)
  clear_has_email();
  return email_.ReleaseNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void Person::set_allocated_email(::std::string* email) {
  if (email != NULL) {
    set_has_email();
  } else {
    clear_has_email();
  }
  email_.SetAllocatedNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), email);
  // @@protoc_insertion_point(field_set_allocated:Person.email)
}

// repeated .Person.PhoneNumber phone = 4;
inline int Person::phone_size() const {
  return phone_.size();
}
inline void Person::clear_phone() {
  phone_.Clear();
}
inline const ::Person_PhoneNumber& Person::phone(int index) const {
  // @@protoc_insertion_point(field_get:Person.phone)
  return phone_.Get(index);
}
inline ::Person_PhoneNumber* Person::mutable_phone(int index) {
  // @@protoc_insertion_point(field_mutable:Person.phone)
  return phone_.Mutable(index);
}
inline ::Person_PhoneNumber* Person::add_phone() {
  // @@protoc_insertion_point(field_add:Person.phone)
  return phone_.Add();
}
inline ::google::protobuf::RepeatedPtrField< ::Person_PhoneNumber >*
Person::mutable_phone() {
  // @@protoc_insertion_point(field_mutable_list:Person.phone)
  return &phone_;
}
inline const ::google::protobuf::RepeatedPtrField< ::Person_PhoneNumber >&
Person::phone() const {
  // @@protoc_insertion_point(field_list:Person.phone)
  return phone_;
}

// -------------------------------------------------------------------

// AddressBook

// repeated .Person person = 1;
inline int AddressBook::person_size() const {
  return person_.size();
}
inline void AddressBook::clear_person() {
  person_.Clear();
}
inline const ::Person& AddressBook::person(int index) const {
  // @@protoc_insertion_point(field_get:AddressBook.person)
  return person_.Get(index);
}
inline ::Person* AddressBook::mutable_person(int index) {
  // @@protoc_insertion_point(field_mutable:AddressBook.person)
  return person_.Mutable(index);
}
inline ::Person* AddressBook::add_person() {
  // @@protoc_insertion_point(field_add:AddressBook.person)
  return person_.Add();
}
inline ::google::protobuf::RepeatedPtrField< ::Person >*
AddressBook::mutable_person() {
  // @@protoc_insertion_point(field_mutable_list:AddressBook.person)
  return &person_;
}
inline const ::google::protobuf::RepeatedPtrField< ::Person >&
AddressBook::person() const {
  // @@protoc_insertion_point(field_list:AddressBook.person)
  return person_;
}

#endif  // !PROTOBUF_INLINE_NOT_IN_HEADERS
// -------------------------------------------------------------------

// -------------------------------------------------------------------

// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)

#ifndef SWIG
namespace google {
namespace protobuf {

template <> struct is_proto_enum< ::Person_PhoneType> : ::google::protobuf::internal::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::Person_PhoneType>() {
  return ::Person_PhoneType_descriptor();
}

}  // namespace protobuf
}  // namespace google
#endif  // SWIG

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_examples_2fmsg_2eproto__INCLUDED