# Copyright (c) 2009, Digital Enterprise Research Institute (DERI),
# NUI Galway
# All rights reserved.

# author: Cosmin Basca
# email: cosmin.basca@gmail.com

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer
#      in the documentation and/or other materials provided with
#      the distribution.
#    * Neither the name of DERI nor the
#      names of its contributors may be used to endorse or promote
#      products derived from this software without specific prior
#      written permission.

# THIS SOFTWARE IS PROVIDED BY DERI ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL DERI BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
# OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

# -*- coding: utf-8 -*-
__author__ = 'Cosmin Basca'

""" Conditionally import rdflib classes. """

import rdflib

# 2.4 style imports
if rdflib.__version__.startswith("2.4"):
    from rdflib.BNode import BNode
    from rdflib.Graph import Graph, ConjunctiveGraph
    from rdflib.Literal import Literal
    from rdflib.Namespace import Namespace
    from rdflib.Namespace import Namespace as ClosedNamespace
    from rdflib.URIRef import URIRef

    from rdflib.RDF import RDFNS as RDF
    from rdflib.RDFS import RDFSNS as RDFS

# 3.0 style imports
if rdflib.__version__.startswith("2.5") or rdflib.__version__.startswith("3.0"):
    from rdflib.term import BNode
    from rdflib.graph import Graph, ConjunctiveGraph
    from rdflib.term import Literal
    from rdflib.namespace import ClosedNamespace, Namespace
    from rdflib.namespace import RDF, RDFS
    from rdflib.term import URIRef

# 4.0 style imports
if rdflib.__version__.startswith("4"):
    from rdflib.term import BNode
    from rdflib.graph import Graph, ConjunctiveGraph
    from rdflib.term import Literal
    from rdflib.namespace import ClosedNamespace, Namespace
    from rdflib.namespace import RDF, RDFS
    from rdflib.term import URIRef

__exports__ = [BNode, ClosedNamespace, ConjunctiveGraph, Graph, Literal,
               Namespace, RDF, RDFS, URIRef]
