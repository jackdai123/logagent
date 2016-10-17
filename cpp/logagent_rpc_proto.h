#pragma once

#include <string>
#include <list>
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

	class opqueryreq {
		public:
			std::string user;
			int begintime;
			int endtime;

		public:
			MSGPACK_DEFINE(user, begintime, endtime);
	};

	class opqueryres {
		public:
			std::list<opmsg> oplogs;

		public:
			MSGPACK_DEFINE(oplogs);
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
