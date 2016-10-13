#include <exception>
#include "logagent_rpc_handler.h"

namespace logagent {

	void logagent_rpc_handler :: dispatch( msgpack_stream stream ) {
		try {
			std::string method;
			stream.method().convert(&method);

			if (method == "critical") {
				msgpack::type::tuple< debugmsg > req;
				stream.params().convert(&req);
				this->critical( stream, req.get<0>() );
			} else if (method == "error") {
				msgpack::type::tuple< debugmsg > req;
				stream.params().convert(&req);
				this->error( stream, req.get<0>() );
			} else if (method == "warning") {
				msgpack::type::tuple< debugmsg > req;
				stream.params().convert(&req);
				this->warning( stream, req.get<0>() );
			} else if (method == "info") {
				msgpack::type::tuple< debugmsg > req;
				stream.params().convert(&req);
				this->info( stream, req.get<0>() );
			} else if (method == "debug") {
				msgpack::type::tuple< debugmsg > req;
				stream.params().convert(&req);
				this->debug( stream, req.get<0>() );
			} else if (method == "opreport") {
				msgpack::type::tuple< opmsg > req;
				stream.params().convert(&req);
				this->opreport( stream, req.get<0>() );
			} else if (method == "webreport") {
				msgpack::type::tuple< webmsg > req;
				stream.params().convert(&req);
				this->webreport( stream, req.get<0>() );
			} else if (method == "busireport") {
				msgpack::type::tuple< busimsg > req;
				stream.params().convert(&req);
				this->busireport( stream, req.get<0>() );

			} else {
				stream.error( msgpack::rpc::NO_METHOD_ERROR );
			}
		} catch( msgpack::type_error & e ) {
			stream.error( msgpack::rpc::ARGUMENT_ERROR );
		} catch( std::exception & e ) {
			stream.error( std::string(e.what()) );
		}
	}

	void logagent_rpc_handler :: critical( msgpack_stream stream, const debugmsg & req ) {
		//add logic code

	}

	void logagent_rpc_handler :: error( msgpack_stream stream, const debugmsg & req ) {
		//add logic code

	}

	void logagent_rpc_handler :: warning( msgpack_stream stream, const debugmsg & req ) {
		//add logic code

	}

	void logagent_rpc_handler :: info( msgpack_stream stream, const debugmsg & req ) {
		//add logic code

	}

	void logagent_rpc_handler :: debug( msgpack_stream stream, const debugmsg & req ) {
		//add logic code

	}

	void logagent_rpc_handler :: opreport( msgpack_stream stream, const opmsg & req ) {
		//add logic code

	}

	void logagent_rpc_handler :: webreport( msgpack_stream stream, const webmsg & req ) {
		//add logic code

	}

	void logagent_rpc_handler :: busireport( msgpack_stream stream, const busimsg & req ) {
		//add logic code

	}

}