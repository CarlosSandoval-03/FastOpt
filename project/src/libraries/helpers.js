const bcrypt = require("bcryptjs");

const helpers = {};

helpers.encryptPassword = async (password) => {
	const salt = await bcrypt.genSalt(10);
	const hash = await bcrypt.hash(password, salt);
	return hash;
};

helpers.matchPassword = async (password, hash) => {
	return await bcrypt.compare(password, hash);
};

module.exports = helpers;
