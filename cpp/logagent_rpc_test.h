#pragma once

#include "opt_map.h"

namespace logagent {

	class TestTool {
		public:
			TestTool();
			virtual ~TestTool();

		public:
			virtual int critical( OptMap & bigmap );
			virtual int error( OptMap & bigmap );
			virtual int warning( OptMap & bigmap );
			virtual int info( OptMap & bigmap );
			virtual int debug( OptMap & bigmap );
			virtual int opreport( OptMap & bigmap );
			virtual int webreport( OptMap & bigmap );
			virtual int busireport( OptMap & bigmap );

		public:
			typedef int (TestTool::*ToolFunc_t) ( OptMap & );

			typedef struct tagName2Func {
				const char * name;
				TestTool::ToolFunc_t func;
				const char * opt_string;
				const char * usage;
			} Name2Func_t;

			static Name2Func_t * GetName2Func()
			{
				static Name2Func_t name2func [] = {
					{ "critical", &TestTool::critical, "c:f:h", "" },
					{ "error", &TestTool::error, "c:f:h", "" },
					{ "warning", &TestTool::warning, "c:f:h", "" },
					{ "info", &TestTool::info, "c:f:h", "" },
					{ "debug", &TestTool::debug, "c:f:h", "" },
					{ "opreport", &TestTool::opreport, "c:f:h", "" },
					{ "webreport", &TestTool::webreport, "c:f:h", "" },
					{ "busireport", &TestTool::busireport, "c:f:h", "" },

					{ NULL, NULL }
				};

				return name2func;
			};
	};


	class TestToolImpl : public TestTool {
		public:
			TestToolImpl();
			virtual ~TestToolImpl();

		public:
			virtual int critical( OptMap & bigmap );
			virtual int error( OptMap & bigmap );
			virtual int warning( OptMap & bigmap );
			virtual int info( OptMap & bigmap );
			virtual int debug( OptMap & bigmap );
			virtual int opreport( OptMap & bigmap );
			virtual int webreport( OptMap & bigmap );
			virtual int busireport( OptMap & bigmap );

	};

}
