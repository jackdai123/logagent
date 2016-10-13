#pragma once

#include <string>
#include <msgpack.hpp>

namespace logagent {

	class debugmsg {
		public:
			std::string value;

		public:
			MSGPACK_DEFINE(value);
	};

	class opmsg {
		public:
			int time;
			std::string user;
			std::string action;
			std::string args;
			std::string others;

		public:
			MSGPACK_DEFINE(time, user, action, args, others);
	};

	class webmsg {
		public:
			int time;
			std::string clientip;
			std::string url;
			int status;
			int runtime;

		public:
			MSGPACK_DEFINE(time, clientip, url, status, runtime);
	};

	class busimsg {
		public:
			int time;
			std::string svrname;
			std::string api;
			std::string args;
			std::string status;
			int runtime;

		public:
			MSGPACK_DEFINE(time, svrname, api, args, status, runtime);
	};

}