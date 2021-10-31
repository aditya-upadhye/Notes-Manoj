//mongodb lib
import 'package:mongo_dart/mongo_dart.dart';
//to get environment variable
import 'package:dotenv/dotenv.dart' show load, env;

// Importing the dart package for input
import 'dart:io';

Future insertData(DbCollection collection) async {
  print("\nEnter the name");
  String? name = stdin.readLineSync();

  print("Enter the email id");
  String? email = stdin.readLineSync();

  print("Enter the age");
  String age = stdin.readLineSync() ?? '0';

  print("\nInserting data the data in mongodb");
  print("==================================");

  Map<String, dynamic> data = {
    'email': email,
    'name': name,
    'age': int.parse(age),
    'Admin': false
  };

  var inserted = await collection.insertOne(data);
  print(inserted.id);
  return inserted;
}

Future makeAdmin(WriteResult inserted, DbCollection collection) async {
  print("[ID]: " + inserted.id.toString());
  print("\nNext: Making the user as Admin");
  print("==============================");
  print("Press ENTER to proceed");
  stdin.readLineSync();

  await collection.updateOne(
      where.eq('_id', inserted.id), modify.set('Admin', true));
  print("Updated");
}

Future insertMultipleData(DbCollection collection) async {
  print("\nInsert Multiple Data");
  print("====================");

  print("\n\tEnter the number of data to inserted");
  String _n = stdin.readLineSync() ?? '0';
  int n = int.parse(_n);

  List<Map<String, dynamic>> datas = [];
  for (var i = 0; i < n; i++) {
    print("\nEnter the name");
    String? name = stdin.readLineSync();

    print("Enter the email id");
    String? email = stdin.readLineSync();

    print("Enter the age");
    String age = stdin.readLineSync() ?? '0';
    datas.add({
      'email': email,
      'name': name,
      'age': int.parse(age),
      'Admin': false,
    });
  }
  await collection.insertMany(datas);
  print("\nData $n is inserted");
}

Future makeAdmins(DbCollection collection) async {
  await collection.updateMany(
    where.gt('age', 50),
    modify.set('Admin', true),
  );
  print("All the people above 50 are made as ADMIN");
}

Future findMinors(DbCollection collection) async {
  var datas = await collection.find(where.lt('age', 18)).toList();
  print("People under 18:");
  print(datas);
}

Future removeMinors(DbCollection collection) async {
  var datas = await collection.deleteMany(where.lt('age', 18));
  print("Datas are removed");
}

void main(List<String> arguments) async {
  // loading environment variables
  load();
  String uri = env['MONGO_URI'] ?? 'PASTE THE URI';

  print("\nConnecting to MongoDB");
  print("====================");
  var db = await Db.create(uri);
  await db.open();
  print("\nConnected");
  print(db.serverStatus());
  var collection = db.collection('users');

  // Inserting single data
  dynamic inserted = await insertData(collection);

  // Updating previous user as Admin
  await makeAdmin(inserted, collection);

  // Inserting multiple datas
  insertMultipleData(collection);

  // Making 50+ years people as ADMIN
  await makeAdmins(collection);

  // Finding users under age 18
  await findMinors(collection);

  // Delete all minors from collection
  await removeMinors(collection);

  db.close();
}
