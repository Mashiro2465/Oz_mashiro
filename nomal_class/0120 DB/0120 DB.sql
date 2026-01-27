use test;

CREATE TABLE PetOwners(
	ownerId int AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    contact VARCHAR(100)
    );

CREATE TABLE Pets (
    petID int AUTO_INCREMENT PRIMARY KEY,
    ownerId int,
    name VARCHAR(100),
    species VARCHAR(100),
    breed VARCHAR(100),
    FOREIGN KEY (ownerId) REFERENCES PetOwners(ownerId)
);

CREATE TABLE Rooms(
	roomID int AUTO_INCREMENT PRIMARY KEY,
    roomNumber VARCHAR(50),
    roomType VARCHAR(50),
    pricePerNight DECIMAL(10,2)
);

CREATE TABLE Reservations(
	reservationID int AUTO_INCREMENT PRIMARY KEY,
    petID int, 
    roomID int,
    startDate DATE,
    endDate DATE,
    FOREIGN KEY(petID) REFERENCES Pets(petID),
    FOREIGN KEY(roomID) REFERENCES Rooms(roomID)
);

CREATE TABLE Services(
	service int AUTO_INCREMENT PRIMARY KEY,
    reservationID int,
    serviceName VARCHAR(50),
    servicePrice DECIMAL(10,2),
    FOREIGN KEY(reservationID) REFERENCES Reservations(reservationID)
);