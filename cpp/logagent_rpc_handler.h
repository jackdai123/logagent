#pragma once

#include <jubatus/msgpack/rpc/server.h>
#include "logagent_rpc_proto.h"

namespace logagent {

	class logagent_rpc_handler : public msgpack::rpc::dispatcher {
		public:
			typedef msgpack::rpc::request msgpack_stream;

		public:
			void dispatch( msgpack_stream stream );

		public:
			void critical( msgpack_stream stream, const debugmsg & req );
			void error( msgpack_stream stream, const debugmsg & req );
			void warning( msgpack_stream stream, const debugmsg & req );
			void info( msgpack_stream stream, const debugmsg & req );
			void debug( msgpack_stream stream, const debugmsg & req );
			void opreport( msgpack_stream stream, const opmsg & req );
			void webreport( msgpack_stream stream, const webmsg & req );
			void busireport( msgpack_stream stream, const busimsg & req );
	};

}